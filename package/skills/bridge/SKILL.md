---
name: bridge
description: Use when the user wants something a real doctor or pharmacist can look at, including the whole story for a new clinician, or when a professional's reply has come back, and the Advolog core is present. Carries a minimized summary out and records what came back. Does no research. Does not send anything. Not when the Advolog core is absent.
---

# Bridge

The two-way loop with real professionals. Outbound carries a minimized summary the person sends. Inbound records exactly what came back. This skill does no research.

Act only when the Advolog core is present. Otherwise do nothing special.

Read `profile.md` (including the trusted-clinician answer, the alias, and the consent note), `medications.md` in full including recent stops, recent `symptoms.md`, `open-questions.md`, and `professional-review.md`.

## Outbound

If the consent note is empty and the record is for someone else, ask once, plainly, and produce nothing outbound until they answer.

Frame by the trusted-clinician answer. A trusted clinician can run the questions in their own professional context, and what comes back is recorded with honest labels. No trusted clinician: say the honest reframe [UF]. These questions touch resources the doctor has. Sending them to a consumer AI is possible, and whatever returns will be labeled honestly, but the stronger move is bringing them to the doctor as questions.

Build one self-contained block they can paste whole [UF]: alias, situation line, age or sex only if it changes the professional's answer (ask now if missing, once), the full current list with recent stops flagged, recent symptoms with the logged severities, their worries in their words, and the ask. A reply in the professional's own words is fully enough. Citations are requested, never demanded. Focused blocks follow only if they fit.

Strip identifiers per the core. Run the checklist. Save a dated copy in `reports/`. Hand it to the person. Never send it. Never call it de-identified.

When the professional is new to the case, the artifact is the whole-story digest, one to two pages, hard cap. Order: situation line, history in brief (timeline compressed, chronological), medications now and tried with outcomes, current pattern, professional findings (empty stays visibly empty), top open questions, what this document is. Same gates.

A one-page handover for another family member is not a separate path in this version. The whole-story digest, with the same gates, is what you offer if they ask for a page someone else in the family can hold. Do not add clinical claims to make it more useful.

## Inbound

Record in `professional-review.md` exactly what was said: who (role, name optional), asked, reported (their words or a faithful summary), via which system if stated, date. Empty fields stay empty. Do not flatten severity. Questions the reply raises go to the ledger. One warm line: this is how the record gets stronger. [UF]

No generated findings. No simulated professional output. Nobody is asked to break an institutional rule.
