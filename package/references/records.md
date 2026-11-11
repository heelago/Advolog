# Record schemas

<!-- Additive only. A file written by 1.0 or 1.1 still reads. New fields may appear.
     Absence of a newer field means "predates it", never an error.
     Header lines: the current wording is in report-templates.md. A header already
     in someone's file, including one that used an em dash, stays. Do not rewrite it. -->

Every record: a title line, one line saying what it is, one line saying both ways to fill it and that it is theirs to edit, then `עודכן לאחרונה: DD.MM.YYYY · <one-word tag>`. Newest entries first. Nothing is deleted by normal use. Stopped medications move to Stopped with date and the reason as recorded. Answered questions keep their answers. Corrections are welcome and do not destroy history.

## profile.md

About (display name, one-sentence situation) · Sharing name (outbound alias and what it is for) · Care circle (roles, first names only) · For caregivers (about / maintained-by / consent note) · Preferences (language, guidance level, register, how saving works, anecdote toggle, active paths, accepted automations, settled choices as one dated line each) · Research context (about five optional slots, never required).

The consent note gates outbound artifacts only. Empty means "not answered yet", and the bridge asks once before anything leaves.

## medications.md

**Allergies** sit on top as one field line beginning exactly `אלרגיות:` for example `אלרגיות: לא תועד` / `אלרגיות: אין ידועות (נמסר DD.MM.YYYY)` / `אלרגיות: <list>`. Never a section heading, so every reader finds the same line. A previous value moves to `אלרגיות (קודם):` beneath it. Current: name, dose, frequency, since, prescriber role, reactions. Stopped: date and reason as recorded. To confirm with the pharmacist.

## timeline.md

`DD.MM.YYYY · type · one line · with whom (role)`. Partial dates: `MM.YYYY` or `YYYY`.

Types: encounter, attempt (outcome when known; an optional source-attributed expected-response window, tier-labeled, when research supplied one), change, episode, document (a described reference, nothing copied), note.

## symptoms.md

`date · what · severity · context one-liner`. Severity is exactly one of `קל` / `בינוני` / `קשה`, or left blank. Never a fourth word. "Not recorded" is an empty slot, not a new label.

## open-questions.md

`Q-NN · question · why we're asking (one line; tier label if research-born) · for whom (role) · priority · source · status`.

Sections: Open / Asked / Answered (answer kept) / Deferred / **Set aside by the team** (date and the doctor's stated reason, in their words). A set-aside question is not restarted from zero. It may be offered again only on material new evidence or a real pattern change, once, calmly: "this was set aside when the picture was X; the picture changed. Worth re-raising?" Never nagging.

## professional-review.md

`date · who (role; name optional) · asked · reported (their words or a faithful summary) · via which system, if stated`. Unreported fields stay empty. Emptiness here is honest.

## inbox.md

The header may carry `Capture mode: on · since <date>`. Sections: Capture (raw) · Proposals (`[pending]` / `[accepted <date>]` / `[dismissed]`) · Processed (one-line trail). Nothing in a proposal enters a record without an explicit yes.

## handoff.md

Not a record. Skeleton in `report-templates.md`. Ten lines at most. Each new note replaces the last. It points at the records and carries no clinical content of its own. Absent means nothing pending.

## reports/

Save-once artifacts. Filename `YYYY-MM-DD-<slug>.md`. The date inside the document is still `DD.MM.YYYY`.

## Single file, my-record.md

Equivalent to the seven files. One save per session on the web and on a phone. The seven-file folder remains the layout for a folder install. Do not convert one into the other unless the person asks.

```
# הרשומה שלי
עודכן לאחרונה: DD.MM.YYYY · קובץ

## הפרופיל שלי
<the profile envelope and body>

## תרופות
<the medications envelope, allergy line first>

## ציר הזמן

## יומן תסמינים

## שאלות פתוחות

## ממצאים מאנשי מקצוע

## תיבת קליטה
```

A missing section means not started. The dashboard reads this file when the seven files are absent, and reads the seven files when they are present. If both exist, the seven files win and the dashboard says so. It does not merge them.

Section titles already used in a 1.1 file (`# הפרופיל שלי` and the rest) are the same titles here, so a reader of either layout finds the same headings.

## What this file does not change

No field was removed. No required rewrite. A `deadline` timeline type is not in this version.
