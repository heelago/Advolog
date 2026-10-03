# Unit: prep-sheet

**Triggers:** a booked visit mentioned · "get me ready for the appointment" · the offered close after material changes when a visit exists.

**Purpose:** the one-page sheet the appointment actually runs on. A doctor extracts the situation, the regimen, and the asks inside two minutes.

**Principles:** Substance First · One Small Move (a couple of setup questions at most: which visit, anything that must not go unsaid).

**Setup:** read everything relevant: `profile.md`, `medications.md`, `open-questions.md`, `symptoms.md` and `timeline.md` since the last encounter, `professional-review.md`.

**Workflow:** build `reports/YYYY-MM-DD-prep-<visit-slug>.md`, print-clean, one page [UF throughout]:

```
*[framing line]*                    <name-or-alias by destination> · <situation line> · <visit, date>
**אלרגיות:** <list> | לא תועד      ← always renders; "not recorded" is visible, never omitted
## Questions                        priority order; grouped by role when several; each: the question ·
                                    one-line reasoning · ______ (answer blank)
## Current medications              one line each: name · dose · frequency · since · reactions
                                    recently stopped: flagged, with date — stop-timing matters
## Since last visit                 grouped so patterns show (by theme, not by date)
## Tried and what happened          attempts table (from timeline) — the diagnostic spine when present
## To confirm                       pharmacist items from medications.md
## Notes                            blank space; the sheet expects handwriting
```

- Pre-share checklist runs before delivery (map §11). Questions come from the ledger; a stale ledger gets the questions unit's pass first.
- Null state is a real product: with a thin record, ship the structured sheet anyway — an allergy line and one good question already work; pin the after-hours/triage line at top when urgency context exists.
- **Rehearsal mode** (rehearsal intent, or on request): add — or produce standalone — the likely-questions section: what the doctor will probably ask at this kind of visit, each with a prepared-answer blank and one line on why doctors ask it (advocacy training, shared with the questions unit; source-attributable where sourced).
- The sheet is a save-once artifact; asked-status updates happen at debrief, not now.
- **A file to hand over (map §5):** where this session offers a native document that exports to Word or PDF, produce the sheet there, and say once [UF]: it is private until you share it, and a shared link is one tap away — so for the doctor, export the file and hand that over. The `reports/` copy stays the record. Where no such document exists, the output is unchanged; which platforms have one is in the setup guides.
- **Setting:** this unit reads the whole record. Where the user has a higher effort or thinking setting, one line before building says it is worth switching on for this — once, then proceed either way (map §10).

**Constraints echo:** nothing on the sheet interprets; observed patterns are presented as observations; every clinical fact traces to a record entry; identifiers per map §11 minimization.
