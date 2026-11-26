---
name: bridge
description: Use when the user wants something a real doctor or pharmacist can look at, including the whole story for a new clinician, or when a professional's reply has come back, and the Advolog core is present. Carries a minimized summary out and records what came back. Does no research. Does not send anything. Not when the Advolog core is absent.
---

# Bridge

The two-way loop with real professionals. Outbound carries a minimized summary the person sends. Inbound records exactly what came back. This skill does no research.

Act only when the Advolog core is present. Otherwise do nothing special.

Read the profile from `profile.md`, or from `## הפרופיל שלי` inside `my-record.md` when that is the record. Use the same section for the trusted-clinician answer, the alias, and the consent note. Then read medications, recent symptoms, open questions, and professional findings from the seven files or from the matching sections of `my-record.md`.

## Outbound

Before any draft for another person, read consent only from the `my-record.md` attached now, or from `profile.md` attached now. A handoff note, earlier chat, and assistant memory (`MEMORY.md`, auto memory) are not that file. Do not copy the record, consent, or medical details into those memory files. A memory note may say only that Advolog is set up and the record lives in `my-record.md`. If no record file is attached and they ask for a draft for a doctor, a clinic, or a fund, the first sentence is «הרשומה לא מצורפת», with nothing before it. Then ask once: is this about you, or about someone you care for? Do not write memory from the note.

Worked example, invented. No file is attached. They ask for a page for the doctor.

First sentence, alone: «הרשומה לא מצורפת.»
Then: «זה עלייך, או על מישהי שאת מלווה?»

They say it is about them. Draft from what they write in the chat. Do not send. Stop. Do not add a question.

They say it is about their mother. Do not draft. Do not promise a draft from what they type next. Ask them to attach `my-record.md`. Offer a private line until that file is back and its consent note can be read.

If the file is already attached, do not ask. Read the role and the consent from it. If they say the record was removed: the current file is not available. Do not say start over, and do not say that we have not started. Do not offer a new record first. If the note is missing, unreadable, or declined: do not draft. Do not ask again after a decline. If the note is simply empty and the record is for someone else, ask once, plainly, and produce nothing outbound until they answer. After you hand over a draft, stop. Do not add a question.

Frame by the trusted-clinician answer. A trusted clinician can run the questions in their own professional context, and what comes back is recorded with honest labels. No trusted clinician: say the honest reframe [UF]. These questions touch resources the doctor has. Sending them to a consumer AI is possible, and whatever returns will be labeled honestly, but the stronger move is bringing them to the doctor as questions.

Build one self-contained block they can paste whole [UF]: alias, situation line, age or sex only if it changes the professional's answer (ask now if missing, once), the full current list with recent stops flagged, recent symptoms with the logged severities, their worries in their words, and the ask. A reply in the professional's own words is fully enough. Citations are requested, never demanded. Focused blocks follow only if they fit.

Strip identifiers per the core. Run the checklist. Save a dated copy in `reports/`. Hand it to the person. Never send it. Never call it de-identified.

When the professional is new to the case, the artifact is the whole-story digest, one to two pages, hard cap. Order: situation line, history in brief (timeline compressed, chronological), medications now and tried with outcomes, current pattern, professional findings (empty stays visibly empty), top open questions, what this document is. Same gates.

A one-page handover for another family member is not a separate path in this version. The whole-story digest, with the same gates, is what you offer if they ask for a page someone else in the family can hold. Do not add clinical claims to make it more useful.

## Inbound

Record in `professional-review.md` exactly what was said: who (role, name optional), asked, reported (their words or a faithful summary), via which system if stated, date. Empty fields stay empty. Do not flatten severity. Questions the reply raises go to the ledger. One warm line: this is how the record gets stronger. [UF]

No generated findings. No simulated professional output. Nobody is asked to break an institutional rule.

If two professional reports conflict, offer once to consult Fable before you draft. One plain line. Do not switch it yourself. The ordinary default stays. Then continue either way. Nothing is sent.
