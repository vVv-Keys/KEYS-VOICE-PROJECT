# KEYS VOICE PROJECT

Portable vocal-identity research and production system for **Keys / Sky Desperado**.

The permanent asset is the clean, human-recorded voice dataset. Suno, Seed-VC,
future conversion engines, and TapeRoom are replaceable consumers of that asset.

## Goals

- Preserve a canonical, untouched `KEYS_VOICE_MASTER_v1` dataset.
- Build reproducible Suno Voice and Custom Model references.
- Evaluate local singing voice-conversion models against fixed benchmarks.
- Add an offline/HQ Voice Identity workflow to TapeRoom only after the model is stable.
- Keep raw voice data private and prevent accidental commits of sensitive audio.

## Pipeline

```text
RAW MASTER -> BACKUP -> CLEAN -> SEGMENTED -> TRAIN / VALIDATION / TEST
                                              |
                         SUNO / LOCAL VC / TAPEROOM
                                              |
                                  SKY DESPERADO OUTPUT
```

## Start here

1. Complete the two-microphone comparison in [`docs/PILOT_SESSION_V1.md`](docs/PILOT_SESSION_V1.md).
2. Choose the canonical microphone only after reviewing both unprocessed tests.
3. Record the 15–20 minute pilot on the chosen microphone.
4. Copy `templates/RECORDING_LOG.csv` to your working audio drive.
5. Run `python scripts/validate_dataset.py /path/to/01_RAW_MASTER`.
6. Run `python scripts/build_manifest.py /path/to/01_RAW_MASTER --output manifests/raw_master_v1.json`.
7. Review failures and listening notes before recording the full session in [`docs/RECORDING_SESSION_V1.md`](docs/RECORDING_SESSION_V1.md).

## Repository boundaries

This repository stores documentation, configurations, scripts, manifests,
prompts, benchmark definitions, and small approved examples. Raw voice recordings,
stems, model checkpoints, BandLab exports, and secrets are ignored by default.
See [`docs/AUDIO_STORAGE.md`](docs/AUDIO_STORAGE.md).

## Core rules

- Never overwrite `01_RAW_MASTER`.
- Never train from the only copy of a recording.
- Never mix Tune, Melodyne, reverb, delay, mastering, or instrumental bleed into the canonical dataset.
- Keep test material unseen during training.
- Version datasets and checkpoints; do not replace a good model in place.
- Keep TapeRoom's proven low-latency tuner independent from experimental voice conversion.

## Status

- [x] Project structure
- [x] Recording protocol v1
- [x] Dataset validator and manifest builder
- [x] Benchmark and recording templates
- [x] Pilot and microphone A/B protocol
- [x] BandLab intake/export protocol
- [x] Automated repository tests
- [ ] Scarlett Studio vs. older condenser A/B test
- [ ] 15–20 minute pilot recording
- [ ] Pilot QA and mic selection
- [ ] Full master dataset
- [ ] Suno reference montage
- [ ] Zero-shot local VC benchmark
- [ ] Fine-tuned Keys checkpoint
- [ ] TapeRoom offline/HQ integration

Private research project. No permission is granted to use the voice data or derived
models outside this project.
