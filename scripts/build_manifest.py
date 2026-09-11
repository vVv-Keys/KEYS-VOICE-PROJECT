#!/usr/bin/env python3
"""Build a privacy-safe, reproducible manifest without copying audio into Git."""

from __future__ import annotations

import argparse
import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path


AUDIO_SUFFIXES = {".wav", ".wave", ".flac", ".aif", ".aiff", ".mp3", ".m4a", ".aac", ".ogg", ".opus"}


def sha256_file(path: Path, chunk_size: int = 1024 * 1024) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        while chunk := handle.read(chunk_size):
            digest.update(chunk)
    return digest.hexdigest()


def build_manifest(root: Path) -> dict:
    files = []
    for path in sorted(p for p in root.rglob("*") if p.is_file() and p.suffix.lower() in AUDIO_SUFFIXES):
        stat = path.stat()
        files.append(
            {
                "relative_path": path.relative_to(root).as_posix(),
                "bytes": stat.st_size,
                "modified_utc": datetime.fromtimestamp(stat.st_mtime, timezone.utc).isoformat(),
                "sha256": sha256_file(path),
            }
        )
    return {
        "schema_version": 1,
        "dataset_root_name": root.name,
        "generated_utc": datetime.now(timezone.utc).isoformat(),
        "file_count": len(files),
        "total_bytes": sum(item["bytes"] for item in files),
        "files": files,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("root", type=Path, help="Root folder containing private audio")
    parser.add_argument("--output", type=Path, required=True, help="Manifest JSON path")
    args = parser.parse_args()

    root = args.root.expanduser().resolve()
    if not root.is_dir():
        parser.error(f"dataset root is not a directory: {root}")

    manifest = build_manifest(root)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")
    print(f"Wrote {manifest['file_count']} files to {args.output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
