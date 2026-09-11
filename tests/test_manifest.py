import tempfile
import unittest
from pathlib import Path

from scripts.build_manifest import build_manifest


class ManifestTests(unittest.TestCase):
    def test_manifest_finds_audio_and_hashes_it(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "take.wav").write_bytes(b"voice-test")
            (root / "ignore.txt").write_text("ignore", encoding="utf-8")
            result = build_manifest(root)
            self.assertEqual(result["file_count"], 1)
            self.assertEqual(result["files"][0]["relative_path"], "take.wav")
            self.assertEqual(len(result["files"][0]["sha256"]), 64)


if __name__ == "__main__":
    unittest.main()
