import struct
import tempfile
import unittest
import wave
from pathlib import Path

from scripts.validate_dataset import validate_wav


class ValidatorTests(unittest.TestCase):
    def test_accepts_24_bit_mono_48k_wav_below_ceiling(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "valid.wav"
            sample = 1_000_000
            frame = struct.pack("<i", sample)[:3]
            with wave.open(str(path), "wb") as target:
                target.setnchannels(1)
                target.setsampwidth(3)
                target.setframerate(48_000)
                target.writeframes(frame * 100)
            self.assertEqual(validate_wav(path), [])


if __name__ == "__main__":
    unittest.main()
