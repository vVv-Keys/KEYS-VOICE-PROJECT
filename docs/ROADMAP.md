# Roadmap

## Phase 0 — Foundation

- Create private repository and permanent folder conventions.
- Record chain, mic, environment, gain, and ownership metadata.
- Capture a 15–20 minute pilot and inspect it before the full session.

## Phase 1 — Canonical dataset

- Record 40–60 usable minutes at 48 kHz / 24-bit / mono.
- Preserve untouched masters and a separate backup.
- Log every take, exclusion, cleanup decision, and source checksum.
- Segment into train (about 85%), validation (about 10%), and truly unseen test (about 5%).

## Phase 2 — Suno assets

- Build a clean two-minute a cappella reference montage.
- Create fixed benchmark songs for natural melodic, melodic rap, hard rap,
  intimate, high-register, and harmony use cases.
- Curate representative owned songs before training a Core Custom Model.
- Archive prompts, settings, outputs, stems, and evaluation notes outside Suno.

## Phase 3 — Independent voice engine

- Benchmark zero-shot Seed-VC or the best permitted singing-VC engine available.
- Fine-tune only if it measurably beats zero-shot conversion.
- Version checkpoints and preprocessing metadata; never overwrite winners.
- Score identity, naturalness, pitch/formant preservation, diction, emotion,
  register behavior, and artifacts against fixed held-out inputs.

## Phase 4 — TapeRoom integration

- First ship an offline/HQ upload-or-record conversion workflow.
- Keep existing pitch correction and Web Audio/Tone.js graph isolated.
- Add streaming conversion only after latency and artifact testing.
- Preserve a bypass path so experimental AI cannot destabilize the working tuner.

## Phase 5 — Production workflow

```text
Human or permitted guide performance
  -> isolated lead stem
  -> Keys Voice Identity engine
  -> pitch/formant cleanup when required
  -> doubles and harmonies
  -> Ableton or TapeRoom vocal chain
  -> master
```

Definition of done: the output remains recognizably the same singer across
melodic singing, melodic rap, straight rap, soft delivery, strong delivery,
and different production styles without depending on one vendor.
