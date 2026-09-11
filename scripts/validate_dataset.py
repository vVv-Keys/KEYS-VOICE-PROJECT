#!/usr/bin/env python3
"""Validate canonical PCM WAV recordings using only the Python standard library."""

from __future__ import annotations

import argparse
import math
import struct
import wave
from pathlib import Path


EXPECTED_RATE = 48_000
EXPECTED_CHANNELS = 1
EXPECTED_WIDTH = 3  # 24-bit PCM


def _max_abs_sample(frames: bytes, sample_width: int) -> int:
    if sample_width == 1:
        return max((abs(value - 128) for value in frames), default=0)
    if sample_width == 2:
        count = len(frames) // 2
        return max((abs(value) for value in struct.unpack(f"<{count}h", frames)), default=0)
    if sample_width == 3:
        peak = 0
        for offset in range(0, len(frames) - 2, 3):
            raw = int.from_bytes(frames[offset : offset + 3], "little", signed=False)
            value = raw - (1 << 24) if raw & (1 << 23) else raw
            peak = max(peak, abs(value))
        return peak
    if sample_width == 4:
        count = len(frames) // 4
        return max((abs(value) for value in struct.unpack(f"<{count}i", frames)), default=0)
    raise ValueError(f"unsupported PCM sample width: {sample_width}")


def peak_dbfs(frames: bytes, sample_width: int) -> float:
    peak = _max_abs_sample(frames, sample_width)
    full_scale = float((1 << (sample_width * 8 - 1)) - 1)
    return -math.inf if peak == 0 else 20.0 * math.log10(peak / full_scale)


def validate_wav(path: Path) -> list[str]:
    errors = []
    try:
        with wave.open(str(path), "rb") as source:
            channels = source.getnchannels()
            width = source.getsampwidth()
            rate = source.getframerate()
            frames = source.readframes(source.getnframes())
    except (wave.Error, EOFError) as exc:
        return [f"invalid WAV: {exc}"]

    if channels != EXPECTED_CHANNELS:
        errors.append(f"channels={channels}; expected {EXPECTED_CHANNELS}")
    if width != EXPECTED_WIDTH:
        errors.append(f"bit_depth={width * 8}; expected {EXPECTED_WIDTH * 8}")
    if rate != EXPECTED_RATE:
        errors.append(f"sample_rate={rate}; expected {EXPECTED_RATE}")

    try:
        peak = peak_dbfs(frames, width)
    except ValueError as exc:
        errors.append(str(exc))
    else:
        if peak >= -0.1:
            errors.append(f"peak={peak:.2f} dBFS; possible clipping")
        elif peak > -3.0:
            errors.append(f"peak={peak:.2f} dBFS; exceeds recommended -3 dBFS ceiling")
    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("root", type=Path)
    args = parser.parse_args()
    root = args.root.expanduser().resolve()
    files = sorted(root.rglob("*.wav")) if root.is_dir() else []
    if not files:
        print(f"No WAV files found under {root}")
        return 2

    failed = 0
    for path in files:
        problems = validate_wav(path)
        if problems:
            failed += 1
            print(f"FAIL {path}")
            for problem in problems:
                print(f"  - {problem}")
        else:
            print(f"PASS {path}")
    print(f"Checked {len(files)} file(s); {failed} failed")
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
