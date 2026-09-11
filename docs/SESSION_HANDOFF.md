# Session handoff

Use this file to continue the voice project without repeating context or
re-uploading the current pilot.

## Current state

- Canonical microphone: **Focusrite Scarlett Studio condenser only**.
- Pilot captured: four raw takes, total duration `16:42.64`.
- Technical QA: `docs/PILOT_QA_REPORT.md`.
- Privacy-safe file inventory: `manifests/pilot_scarlett_v1.json`.
- Raw WAVs remain in private file storage and are not committed to GitHub.
- No derived mono/resampled duplicates have been created.

## Low-usage workflow

- Use a normal ChatGPT conversation for recording direction, listening notes,
  lyric/content planning, and decisions.
- Use Work mode only when repository files, validation scripts, manifests, or
  model code actually need to change.
- In a new normal conversation, provide this repository link and say:
  `Continue KEYS VOICE PROJECT from docs/SESSION_HANDOFF.md.`
- Attach only a new audio batch that has not already been reviewed. Do not attach
  the current four pilot files again; their measurements and hashes are saved.

This workflow avoids duplicate audio storage and avoids spending coding-agent
usage on ordinary recording coaching. It does not make a claim about how an
account's usage meter is calculated; check the current plan meter/support if the
display itself appears incorrect.
