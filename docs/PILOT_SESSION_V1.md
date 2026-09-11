# KEYS Voice Pilot Session v1

Do this before recording the full 40–60 minute master dataset. The immediate
goal is to select one canonical microphone and catch gain, noise, room, diction,
and file-format problems while they are still cheap to fix.

## Equipment under test

- **MIC A:** Focusrite Scarlett Studio condenser microphone.
- **MIC B:** older warm condenser microphone.
- Use the same interface, cable, pop filter, location, posture, and mic distance.
- Each microphone may need its own gain setting. Log both settings; do not force
  identical gain-knob positions.

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
and the strongest peak between -10 and -6 dBFS. Never clip.

## Part 1 — microphone A/B test

Record the exact same material once through each microphone. Do not try to make
the second performance prettier than the first.

### Section 1: natural speech

> Alright, this is my normal voice at a comfortable distance from the microphone.
> I am not trying to make it darker, brighter, deeper, or cleaner. Some words are
> short, some words drag, and the ends of my sentences naturally get quieter.
> This recording should preserve the voice I actually use.

### Section 2: natural melodic voice

Choose one comfortable melody and sing:

> Late light moving through the glass  
> I let another long night pass  
> I do not need to force the sound  
> I only need to stay around

Sing it twice: one normal take and one intimate/quiet take. Do not fully whisper.

### Section 3: melodic rap

Use a silent metronome in headphones around 90 BPM if useful:

> Dashboard glow and the road stay dark  
> Still got miles but I know my mark  
> Built this slow, every piece got proof  
> If it sounds like Keys then it tells the truth

### Section 4: vowels and transitions

- Hold `AH`, `EE`, `OH`, and `OO` for three seconds each.
- Perform one comfortable low-to-middle-to-low siren on `OO`.
- Say `baby`, `pressure`, `different`, `tonight`, `summer`, `crazy`, and `forever`.

### A/B filenames

```text
KVM1_MIC_A_SCARLETT_TEST_RAW.wav
KVM1_MIC_B_WARM_CONDENSER_TEST_RAW.wav
```

Keep the entire test in one file per microphone. Also export a clearly labeled
processed listening copy only if desired; the processed copy is never used to
judge dataset suitability.

## Microphone selection

Score each recording with `templates/MIC_AB_EVALUATION.csv`. Listen for:

- recognizable Keys identity;
- natural low/mid tone without false boom;
- intimate delivery without excessive hiss or air;
- clean consonants without harsh `S`, `T`, or plosives;
- low background noise and electrical hum;
- manageable room/car reflections;
- no crackles, pops, clipping, or unstable cable noise.

Identity and repeatable cleanliness matter more than expensive branding. Do not
select a microphone merely because it sounds louder or brighter.

## Part 2 — 15–20 minute pilot

After choosing one microphone, record these files on that microphone only:

| File | Target | Content |
| --- | ---: | --- |
| `KVM1_SPK_001_Neutral.wav` | 2 min | neutral and conversational speech |
| `KVM1_VOW_001_Pilot.wav` | 2 min | vowels, consonants, attacks, releases |
| `KVM1_PIT_001_Pilot.wav` | 2 min | five-note scales, sustains, slides |
| `KVM1_MEL_001A_Natural.wav` | 3 min | natural mid-register melodic singing |
| `KVM1_BRT_001_Intimate.wav` | 2 min | engaged quiet/intimate delivery |
| `KVM1_MRP_001A_Natural.wav` | 2 min | melodic rap around 80–100 BPM |
| `KVM1_RAP_001A_Conversational.wav` | 2 min | straight conversational rap |
| `KVM1_FREE_001_Performance.wav` | 3 min | original free performance and ad-libs |

Use the matching material in `docs/RECORDING_SESSION_V1.md`. Keep every file raw.

## Stop point

Do not continue into the complete dataset until the pilot has been checked for:

- correct 48 kHz / 24-bit / mono format;
- safe peak level and no clipping;
- consistent mic distance and tone;
- room, traffic, fan, or electrical noise;
- mouth clicks, excessive breath, and plosives;
- sufficient variety without forced high notes;
- filenames and recording log entries.

The pilot is successful when the files are technically clean, recognizably Keys,
comfortable to reproduce, and diverse enough to test a voice model without
contaminating the permanent dataset.
