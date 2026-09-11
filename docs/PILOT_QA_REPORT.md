# Scarlett pilot QA report

**Pilot:** `KVM1_PILOT_SCARLETT_v1`

**Recorded files:** 4

**Total duration:** approximately 17 minutes

**QA date:** 2026-09-11

**Scope:** privacy-safe technical summary; no perceptual/content score yet

## Decision

Keep the Scarlett Studio condenser as the only canonical microphone. Preserve
all four source WAVs unchanged. Do not repeat the same four-minute instructions.

The pilot is useful, but technical checks found insufficient peak headroom and a
noncanonical BandLab source-export format. Keep these files as `SOURCE_RAW` and
build model-ready derivatives only once during later curation. Precise per-file
measurements, hashes, and event timestamps are intentionally not stored in GitHub.

## Next recording settings

1. Keep the Scarlett, mic position, and room fixed.
2. Reduce input gain by at least 6 dB from the clipped setup.
3. Test the loudest planned phrase first; aim for a maximum between -10 and
   -6 dBFS and never 0 dBFS.
4. Avoid touching the microphone, cable, desk, phone, or interface while rolling.
5. Record four different content blocks from `docs/PILOT_SESSION_V1.md`.
6. Upload the next raw batch once. GitHub receives only its privacy-safe status,
   never another copy of the WAVs.

## Current disposition

- Keep all four raw files.
- Do not train directly from the raw pilot.
- Curate clean regions later without modifying the raw masters.
- Complete a listening/content review before assigning clips to training splits.
