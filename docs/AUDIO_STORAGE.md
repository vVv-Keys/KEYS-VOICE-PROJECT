# Audio and model storage

Git is the source of truth for metadata and reproducibility, not the only copy of
the media itself.

## Recommended storage tiers

1. `RAW MASTER`: primary local working drive; immutable after capture.
2. `BACKUP`: second physical or cloud location with matching checksums.
3. `CLEAN/SEGMENTED`: disposable working copies derived from raw masters.
4. `TRAIN/VALIDATION/TEST`: reproducible splits listed in a versioned manifest.
5. `CHECKPOINTS`: private large-file storage with metadata and checksums in Git.

## GitHub policy

Raw audio and model formats are ignored by default. Small, approved examples may
be added only after Git LFS is installed and privacy is reviewed. A Git manifest
records relative path, size, modification time, and SHA-256 without uploading the
recording itself.

## BandLab export convention

For each song export stems from the same exact start point and length:

```text
SONG_SLUG/
  00_SESSION_NOTES/
  01_REFERENCE_MIX/
  02_INSTRUMENTAL/
  03_LEAD_RAW/
  04_LEAD_PRINTED/
  05_DOUBLES/
  06_HARMONIES/
  07_ADLIBS/
  08_MIXES/
  09_MASTERS/
```

File naming:

```text
SKY_[SONG]_[ROLE]_[BPM]_[KEY]_[VERSION]_[YYYY-MM-DD].wav
```

Example:

```text
SKY_POLAROID_SUMMER_LEAD_RAW_96_GMIN_v03_2026-09-11.wav
```

Never bake the instrumental into a dataset vocal. Keep raw and processed vocals
separate, and label AI-generated or converted material explicitly.
