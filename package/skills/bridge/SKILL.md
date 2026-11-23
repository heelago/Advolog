---
name: bridge
description: Use when the user wants something a real doctor or pharmacist can look at, including the whole story for a new clinician, or when a professional's reply has come back, and the Advolog core is present. Carries a minimized summary out and records what came back. Does no research. Does not send anything. Not when the Advolog core is absent.
---

# Bridge

The two-way loop with real professionals. Outbound carries a minimized summary the person sends. Inbound records exactly what came back. This skill does no research.

Act only when the Advolog core is present. Otherwise do nothing special.

Read the profile from `profile.md`, or from `## הפרופיל שלי` inside `my-record.md` when that is the record. Use the same section for the trusted-clinician answer, the alias, and the consent note. Then read medications, recent symptoms, open questions, and professional findings from the seven files or from the matching sections of `my-record.md`.

## Outbound

Before any draft for another person, read consent only from the `my-record.md` attached now, or from `profile.md` attached now. A handoff note, earlier chat, and assistant memory (`MEMORY.md`, auto memory) are not that file. Do not copy the record, consent, or medical details into those memory files. A memory note may say only that Advolog is set up and the record lives in `my-record.md`. If `my-record.md` is not attached, the first sentence is «הרשומה לא מצורפת», before anything else. Do not describe a record you do not have. Do not promise a later draft from what they tell you. Ask them to attach `my-record.md`. Offer a private log. Do not write the note, or any record detail, into memory. If they say the record is gone, removed, or out of date: the current file is not available. Withhold the draft. Say that. Do not say start over, and do not say that we have not started. Do not offer a new record first when one existed. If the note is missing, unreadable, or declined: do not draft. Do not ask again after a decline. If the note is simply empty and the record is for someone else, ask once, plainly, and produce nothing outbound until they answer. After you hand over a draft, stop. Do not add a question.

Frame by the trusted-clinician answer. A trusted clinician can run the questions in their own professional context, and what comes back is recorded with honest labels. No trusted clinician: say the honest reframe [UF]. These questions touch resources the doctor has. Sending them to a consumer AI is possible, and whatever returns will be labeled honestly, but the stronger move is bringing them to the doctor as questions.

Build one self-contained block they can paste whole [UF]: alias, situation line, age or sex only if it changes the professional's answer (ask now if missing, once), the full current list with recent stops flagged, recent symptoms with the logged severities, their worries in their words, and the ask. A reply in the professional's own words is fully enough. Citations are requested, never demanded. Focused blocks follow only if they fit.

Strip identifiers per the core. Run the checklist. Save a dated copy in `reports/`. Hand it to the person. Never send it. Never call it de-identified.

When the professional is new to the case, the artifact is the whole-story digest, one to two pages, hard cap. Order: situation line, history in brief (timeline compressed, chronological), medications now and tried with outcomes, current pattern, professional findings (empty stays visibly empty), top open questions, what this document is. Same gates.

A one-page handover for another family member is not a separate path in this version. The whole-story digest, with the same gates, is what you offer if they ask for a page someone else in the family can hold. Do not add clinical claims to make it more useful.

## Inbound

Record in `professional-review.md` exactly what was said: who (role, name optional), asked, reported (their words or a faithful summary), via which system if stated, date. Empty fields stay empty. Do not flatten severity. Questions the reply raises go to the ledger. One warm line: this is how the record gets stronger. [UF]

No generated findings. No simulated professional output. Nobody is asked to break an institutional rule.

If two professional reports conflict, offer once to switch to the stronger optional model before you draft. One plain line. Do not switch it yourself and do not name a model. The name and the switch are only in `setup/platform-facts.md` if that file is here. Otherwise point at the setup guide and do not guess the name. Then continue either way. Nothing is sent.
