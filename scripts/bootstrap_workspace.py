#!/usr/bin/env python3
"""Create the private local media directories that Git intentionally does not track."""

from pathlib import Path


DIRECTORIES = [
    "01_RAW_MASTER/SPEECH",
    "01_RAW_MASTER/VOWELS",
    "01_RAW_MASTER/ARTICULATION",
    "01_RAW_MASTER/PITCH",
    "01_RAW_MASTER/MELODIC",
    "01_RAW_MASTER/RAP",
    "01_RAW_MASTER/BREATHY",
    "01_RAW_MASTER/POWER",
    "01_RAW_MASTER/HIGH_REGISTER",
    "01_RAW_MASTER/LOW_REGISTER",
    "01_RAW_MASTER/VIBRATO",
    "01_RAW_MASTER/SLIDES",
    "01_RAW_MASTER/ATTACKS",
    "01_RAW_MASTER/RELEASES",
    "01_RAW_MASTER/ADLIBS",
    "01_RAW_MASTER/FREE",
    "01_RAW_MASTER/SONG",
    "02_BACKUP",
    "03_CLEAN",
    "04_SEGMENTED",
    "05_TRAIN",
    "06_VALIDATION",
    "07_TEST",
    "08_SUNO/VOICE_PROFILE",
    "08_SUNO/CUSTOM_MODEL_CORE",
    "08_SUNO/CUSTOM_MODEL_02",
    "08_SUNO/CUSTOM_MODEL_03",
    "08_SUNO/GENERATIONS",
    "09_LOCAL_MODELS/ZERO_SHOT",
    "09_LOCAL_MODELS/KEYS_V1",
    "09_LOCAL_MODELS/KEYS_V2",
    "09_LOCAL_MODELS/CHECKPOINTS",
    "10_BENCHMARKS/NATURAL_MELODIC",
    "10_BENCHMARKS/MELODIC_RAP",
    "10_BENCHMARKS/HARD_RAP",
    "10_BENCHMARKS/INTIMATE",
    "10_BENCHMARKS/HIGH_REGISTER",
    "10_BENCHMARKS/HARMONIES",
    "11_PRODUCTION_TESTS",
    "12_TAPEROOM/OFFLINE_HQ",
    "12_TAPEROOM/REALTIME",
    "12_TAPEROOM/PRESETS",
]


def main() -> None:
    root = Path(__file__).resolve().parents[1]
    for relative in DIRECTORIES:
        (root / relative).mkdir(parents=True, exist_ok=True)
    print(f"Created or verified {len(DIRECTORIES)} private workspace directories under {root}")


if __name__ == "__main__":
    main()
