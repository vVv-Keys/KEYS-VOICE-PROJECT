# KEYS Voice Pilot Session v1

The **Focusrite Scarlett Studio condenser microphone is the only canonical
microphone** for `KEYS_VOICE_MASTER_v1`. There is no microphone A/B step.

The first pilot contains four approximately four-minute Scarlett takes. Do not
record the same instructions again. The next capture should add missing vocal
variety while correcting the level problems documented in
`docs/PILOT_QA_REPORT.md`.

## Environment

Use the quietest repeatable location available.

If recording at home, turn off fans, speakers, television, and notifications.
If the car is the only place where normal singing is possible, park safely with
the engine and climate control off and avoid traffic, rain, and windy locations.
Do not change locations between MIC A and MIC B.

## Capture settings

```text
File:          WAV
Sample rate:   48,000 Hz
Bit depth:     24-bit
Channels:      mono
Normalization: off
Mastering:     off
Track effects: off
Noise gate:    off
Pitch tools:   off
```

Position the microphone 6–8 inches away. Aim normal peaks around -18 to -10 dBFS
and the strongest peak between -10 and -6 dBFS. The first pilot reached 0 dBFS,
so reduce input gain by at least 6 dB and confirm the meter before the next take.

BandLab may export a 44.1 kHz, 16-bit, dual-mono stereo source. Preserve that
original exactly as `SOURCE_RAW`; do not manually upsample it. Canonical mono
48 kHz / 24-bit working files are produced once during later preprocessing.

## Next capture — four different takes

Each take should be about four minutes. Keep the Scarlett position, room, gain,
and posture fixed. Stop immediately if the meter reaches 0 dBFS.

| Take | Content | Direction |
| --- | --- | --- |
| `TAKE_05_SPEECH_ARTICULATION_RAW` | speech, consonants, two emotion lines | normal voice; neutral, hurt, hopeful, confident |
| `TAKE_06_MELODIC_RANGE_RAW` | natural melody, low/mid/high register, sustains, slides | straight tone and natural vibrato; no forced top notes |
| `TAKE_07_RAP_PHRASING_RAW` | melodic rap, straight rap, one line in many cadences | conversational, laid back, harder, ahead/behind beat |
| `TAKE_08_EXPRESSION_FREE_RAW` | intimate, strong, ad-libs, free original performance | engaged quiet voice, full voice, then stop following the script |

Use unused material from `docs/RECORDING_SESSION_V1.md`. One clean take of each
category is more valuable now than another copy of the same pilot script.

## Stop point

Do not continue into the complete dataset until the follow-up has been checked for:

- source format documented and model-ready derivatives planned as 48 kHz / 24-bit / mono;
- safe peak level and no clipping;
- consistent mic distance and tone;
- room, traffic, fan, or electrical noise;
- mouth clicks, excessive breath, and plosives;
- sufficient variety without forced high notes;
- filenames and recording log entries.

The capture is successful when the files are technically clean, recognizably
Keys, comfortable to reproduce, and diverse enough to test a voice model without
contaminating the permanent dataset.
