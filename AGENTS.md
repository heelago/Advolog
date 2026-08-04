# AGENTS.md — working in the Advolog repository

Instructions for any coding agent (or person) working on **this repository**. This is the
public, released project — not a pre-release sandbox. (Note: `package/AGENTS.md` is a different
file — the runtime entrypoint that makes the *tool* work when a user opens the package folder.
This root file is about *contributing to the repo*.)

## What this repo is

Advolog is an open, free toolkit that helps patients and caregivers turn lived medical
experience into structured, credible, doctor-readable material. Layout:

- `package/` — the shipped product: `prompts/core-map.md` (the governing instruction map),
  `prompts/skills/` (fifteen skill units), `prompts/twins/`, `he/` (Hebrew layer), `setup/`,
  `dashboard.html`, `starter/`, and the combined `advolog-chatgpt-bundle.md`.
- `docs/` — the GitHub Pages site (served from `main` `/docs`).
- `README.md`, `LICENSE`, `CONTRIBUTING.md`, `SECURITY.md`, `.github/`.

## The rules that don't bend

Read **`CONTRIBUTING.md`** first — it defines the eleven safety walls. A change that weakens any
of them is rejected regardless of what else it improves. In short: no diagnosis, no treatment
advice, no invented citations, evidence tiers never blended and their fixed Hebrew labels
verbatim, real crisis resources with no methods, the tool never transmits, the user decides
what is kept and shared, and the never-list includes "no AI second opinion."

## Working conventions

- **The map wins.** On any conflict between `package/prompts/core-map.md` and a skill unit, the
  map governs. Behavior changes start in the map.
- **Fixed Hebrew strings are verbatim** (tier labels, framing lines, envelope headers in
  `package/he/report-templates.md`). Don't re-generate them.
- **Schemas evolve additively only** — never a change that forces rewriting a user's records.
- **The ChatGPT bundle is generated**, not hand-edited: change the source files under `package/`
  and regenerate `package/advolog-chatgpt-bundle.md`.
- **Examples are invented only** — nothing describing a real person, even anonymized. Never
  include real medical data anywhere in the repo, issues, or PRs.
- **Regenerate the download** (`docs/advolog.zip`) whenever `package/` changes, and keep
  it byte-aligned with the tree. The archive extracts to a `package/` folder; the one-line
  install prompt on the site tells the assistant to unzip it and read `package/CLAUDE.md`.
- Verify site changes against the live deploy target (GitHub Pages), not just a local file open —
  fonts and some behaviors differ.

## Submitting

Fork → branch → one focused change → PR with three lines (what changed, why, how it was tested).
Prompt changes attach a short invented-persona walk showing the behavior holds. Security issues:
see `SECURITY.md` (private route) — do not open a public issue for a vulnerability.
