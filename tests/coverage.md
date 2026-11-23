# Feature coverage, 1.1 to 1.2

Every 1.1 unit, paste twin, fixed string, gate, and tool has a 1.2 home. Skill names are internal. A person still asks in plain words.

Records are unchanged except for one additive layout: `my-record.md` holds the same seven sections. Existing seven-file folders still read. Old header lines, including those with an em dash, stay valid.

| id | 1.1 home | 1.2 home |
|---|---|---|
| unit:interview | `package/prompts/skills/interview.md` | `package/skills/onboarding/SKILL.md` |
| unit:capture | `package/prompts/skills/capture.md` | `package/skills/capture/SKILL.md` (when it is too much) |
| unit:reconstruction | `package/prompts/skills/reconstruction.md` | `package/skills/capture/SKILL.md` (sorting time) |
| unit:check-in | `package/prompts/skills/check-in.md` | `package/skills/log/SKILL.md` |
| unit:event-logger | `package/prompts/skills/event-logger.md` | `package/skills/log/SKILL.md` |
| unit:research | `package/prompts/skills/research.md` | `package/skills/research/SKILL.md` |
| unit:questions | `package/prompts/skills/questions.md` | `package/skills/questions/SKILL.md` |
| unit:prep-sheet | `package/prompts/skills/prep-sheet.md` | `package/skills/prep/SKILL.md` (full page) |
| unit:express-prep | `package/prompts/skills/express-prep.md` | `package/skills/prep/SKILL.md` (express) |
| unit:interval-summary | `package/prompts/skills/interval-summary.md` | `package/skills/summary/SKILL.md` |
| unit:debrief | `package/prompts/skills/debrief.md` | `package/skills/debrief/SKILL.md` |
| unit:paperwork | `package/prompts/skills/paperwork.md` | `package/skills/paperwork/SKILL.md` |
| unit:bridge | `package/prompts/skills/bridge.md` | `package/skills/bridge/SKILL.md` |
| unit:regimen-chart | `package/prompts/skills/regimen-chart.md` | `package/skills/regimen-chart/SKILL.md` |
| unit:catch-up | `package/prompts/skills/catch-up.md` | `package/skills/continuity/SKILL.md` (catch-up) |
| unit:handoff | `package/prompts/skills/handoff.md` | `package/skills/continuity/SKILL.md` (handoff) |
| twin:capabilities | `package/prompts/twins/capabilities-twin.md` | `package/prompts/capabilities.md` |
| twin:sweep | `package/prompts/twins/sweep-twin.md` | `package/prompts/sweep.md` |
| twin:freshness | `package/prompts/twins/freshness-twin.md` | `package/prompts/freshness.md` |
| twin:wrapup | `package/prompts/twins/wrapup-twin.md` | `package/prompts/wrapup.md` |
| string:tier-labels | core map and `he/report-templates.md` | `package/core.md` and `package/references/report-templates.md`. Labels unchanged: מקורות רשמיים · פרסומים מדעיים · דיווחי מטופלים |
| string:framing | report templates | revised once, em dash removed. Old form declared equivalent in the same file |
| string:source-line | report templates | revised once. Old form declared equivalent |
| string:handoff-why | handoff unit | revised once in `references/report-templates.md`. Old form equivalent |
| string:sync-block | core map §5 | `package/core.md` Saving, and `references/report-templates.md`. First line unchanged |
| string:allergy-line | medications schema, line begins `אלרגיות:` | unchanged in `references/records.md` |
| string:record-headers | `he/report-templates.md` | `references/report-templates.md`. Existing files keep their header |
| string:canon-trap | `he/voice-canon.md` trap answer | `references/voice-canon.md`, em dash removed, meaning unchanged |
| string:canon-distress | voice canon, resource woven once | `references/voice-canon.md` |
| gate:pre-share | core map §11 | `package/core.md` Privacy |
| gate:alias | outbound artifacts | `package/core.md` and `skills/bridge` |
| gate:identifier-strip | core map §11 | `package/core.md` Privacy. Clinicians stay |
| gate:id-number | upload line, never repeat a number | `package/core.md` Privacy |
| gate:caregiver-consent | profile consent note gates outbound only | `package/core.md` and `skills/bridge` |
| gate:anecdote-toggle | first research, once | `package/core.md` record section and `skills/research` |
| gate:provenance-naming | condition only inside a question | wall 1 in `package/core.md`, questions and research skills |
| gate:urgent-cadence | "quickly" reserved for the sign list | `package/core.md` Urgent |
| gate:capture-weave | resource woven, once per sitting | `package/core.md` and `skills/capture` |
| gate:paywall | skip and say so | wall 11 |
| gate:never-transmit | the user sends | wall 7 |
| gate:decline | no second pitch | `package/core.md` first contact and wall 9 |
| gate:no-internal-labels | capability letters never shown | wall 10. The letters themselves are gone |
| tool:dashboard-sync | `package/dashboard.html` sync block | same file. Also reads `my-record.md` when it is the only record |
| tool:dashboard-censor | dashboard censor view | unchanged |
| tool:dashboard-scrub | dashboard text scrub | unchanged |
| tool:dashboard-backup | export button | unchanged. Single-file mode is included in the backup |
| tool:site-censor | `docs/censor.html` | unchanged |
| tool:site-form | `docs/form.html` | unchanged. Onboarding still accepts the paste |
| tool:starter | `package/starter/starter-prompt.md` | same path. No model names. One language block stays under 10,000 characters |

## Not a 1.1 behavior

These are new in 1.2 and do not replace a row above.

- Single-file record `my-record.md`, additive.
- Weekly paste `package/prompts/weekly-log.md`. It asks. It does not write.
- Guideline-options mode, committee skill, letters skill: not in this version. The research skill refuses to rank treatments.
- Agent skill and agent guide: not in this version. `docs/agents.html` names Dot and Grok Bot only, and says Duet is not yet available in Israel.
- Setup instruction: `package/prompts/setup-from-repo.md`, copied from the home page. Hebrew default, English on the second button. The source uses `{{ADVOLOG_RELEASE_REF}}`. The build resolves it to tag `v1.2.0` in `package/web/setup-from-repo.md` and on the home page. The tag is created only at release. A yes fetches the public package only. The assistant checks what is on the screen, suggests a better fit if one is there, and waits. It says where the files landed and gives a downloadable copy when they are not in a real folder. The last step saves `web/instructions.md` where that setup keeps it: Project instructions on a Claude Project, the Instructions field on a classic project or on ChatGPT, or a reopened `package/` folder. `core.md` still wins after setup.
- Two-chat caregiver check: `tests/two-chat-caregiver.md`. Invented record. ChatGPT and Claude. Download waits for a yes. The next chat reopens the record. A missing or declined consent note withholds the outbound draft and keeps private logging. Diagnosis, medication change, identifiers, and sending stay refused. Live run pending.
- Fallback when there is no web access or no file creation: paste `core.md` (7,000-character cap) and upload one modules file. The zip is no longer the primary path.
- Stronger optional model: offered once inside research, full prep, questions, paperwork, and bridge. The skills do not name it. The name and the Claude switch are only in `platform-facts.md` and the rendered model paragraphs.
