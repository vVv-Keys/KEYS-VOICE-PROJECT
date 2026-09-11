# BandLab intake and export protocol

BandLab is a session source, not the permanent archive. The goal is to preserve
original performances while making every export understandable outside BandLab.

## Dataset recordings

1. Duplicate the BandLab project before changing effects or routing.
2. Disable AutoPitch, effects, automation, mastering, and normalization.
3. Export the original mono vocal as WAV when available.
4. Export processed listening copies separately and label them `PRINTED`.
5. Never combine an instrumental, double, harmony, or Suno vocal with a dataset file.
6. Record the BandLab project name and revision in `templates/RECORDING_LOG.csv`.

If BandLab provides only a 44.1 kHz / 16-bit stereo WAV, keep it unchanged as
`SOURCE_RAW`. If the two channels are identical, record that fact in the manifest
but do not create another persistent mono copy yet. Downmix/resample exactly once
when model-ready derivatives are built. Upload each raw batch only once.

## Existing songs and stems

Export every stem from the same timeline start and with the same total duration.
Do not trim each vocal independently; that causes the doubled words, gaps, and
sync drift that make later reconstruction unreliable.

Use this layout:

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

Use one centered primary lead. Keep doubles, harmonies, AI choir layers, and
converted vocals separate. Label every Suno or other synthetic source explicitly.

## Filename

```text
SKY_[SONG]_[ROLE]_[BPM]_[KEY]_[VERSION]_[YYYY-MM-DD].wav
```

Example:

```text
SKY_POLAROID_SUMMER_LEAD_RAW_96_GMIN_v03_2026-09-11.wav
```

## What to provide for organization

- reference mix;
- instrumental;
- every isolated vocal track;
- BPM and key if known;
- lyrics or session notes;
- which version currently sounds best;
- which tracks are human, Suno, converted, tuned, or otherwise processed.

Do not upload raw audio to GitHub. GitHub stores the inventory, notes, checksums,
and reproducibility metadata; the recordings remain in private audio storage.
