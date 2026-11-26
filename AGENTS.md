# AGENTS.md — working in the Advolog repository

Instructions for any coding agent (or person) working on **this repository**. This is the
public, released project — not a pre-release sandbox. (Note: `package/AGENTS.md` is a different
file — the runtime entrypoint that makes the *tool* work when a user opens the package folder.
This root file is about *contributing to the repo*.)

## What this repo is

Advolog is an open, free toolkit that helps patients and caregivers turn lived medical
experience into structured, credible, doctor-readable material. Layout:

- `package/` — the shipped product: `core.md` (the constitution), `skills/` (twelve skills),
  `references/` (Hebrew layer and record schemas), `prompts/` (paste texts), `web/` (generated),
  `setup/`, `dashboard.html`, `starter/`, and the generated `advolog-chatgpt-bundle.md`.
- `docs/` — the GitHub Pages site (served from `main` `/docs`).
- `README.md`, `CHANGELOG.md`, `LICENSE`, `CONTRIBUTING.md`, `SECURITY.md`, `.github/`.

## The rules that don't bend

Read **`CONTRIBUTING.md`** first — it defines the eleven safety walls. A change that weakens any
of them is rejected regardless of what else it improves. In short: no diagnosis, no treatment
advice, no invented citations, evidence tiers never blended and their fixed Hebrew labels
verbatim, real crisis resources with no methods, the tool never transmits, the user decides
what is kept and shared. A question a person chooses to take to a consumer AI, honestly labeled, is the bridge. This tool does not give a second opinion.

## Working conventions

- **The core wins.** On any conflict between `package/core.md` and a skill, the core governs.
  Behavior changes start in the core.
- **Fixed Hebrew strings are verbatim** (tier labels, framing lines, envelope headers in
  `package/references/report-templates.md`). The 1.2 revision removed em dashes once. Older forms already in a file stay valid.
- **Schemas evolve additively only** — never a change that forces rewriting a user's records.
- **The ChatGPT bundle is generated**, not hand-edited: change the source files under `package/`
  and regenerate `package/advolog-chatgpt-bundle.md`.
- **Examples are invented only** — nothing describing a real person, even anonymized. Never
  include real medical data anywhere in the repo, issues, or PRs.
- **Regenerate the download** (`docs/advolog.zip`) whenever `package/` changes, and keep
  it byte-aligned with the tree. The archive extracts to a `package/` folder; the one-line
  install prompt on the site tells the assistant to unzip it and read `package/CLAUDE.md`.
- **Platform facts are dated and sourced.** Model names, plan limits, and feature availability live
  only in `package/setup/platform-facts.md` and the blocks generated from it. Never in the core or the skills. Check each against the platform's own help pages
  before writing it, and move the date in `support-matrix.md`.
- **Every release gets a `CHANGELOG.md` entry** (Hebrew first, English second) and a version line
  in `support-matrix.md`.
- Verify site changes against the live deploy target (GitHub Pages), not just a local file open —
  fonts and some behaviors differ.

## Submitting

Fork → branch → one focused change → PR with three lines (what changed, why, how it was tested).
Prompt changes attach a short invented-persona walk showing the behavior holds. Security issues:
see `SECURITY.md` (private route) — do not open a public issue for a vulnerability.
