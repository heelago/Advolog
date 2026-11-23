#!/usr/bin/env python3
"""Release checks for Advolog. Plain Python, no dependencies.

    python3 tools/check.py

Fails on em dashes in patient-facing copy, a Hebrew/English span mismatch,
a drifted fixed string, a model name outside platform-facts.md, a dead
internal link, a 1.1 unit with no coverage row, or a generated file that
does not match tools/build.py. The Instructions paste must stay within
Heela's 7,000-character cap. A statistic on docs/why.html must have a
row in marketing/sources.md. A graphic that uses D33 or D34 must say
on its face that the wait is for the doctor the patient chose.
why.html is optional until the graphics exist.
"""

from __future__ import annotations

import re
import sys
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))

import build  # noqa: E402

EM = "\u2014"
MODEL_RE = re.compile(
    r"GPT-\d|gpt-\d|\bSonnet\b|\bOpus\b|\bFable\b|\bHaiku\b|\bMythos\b|"
    r"\bLuna\b|\bAstra\b|claude-(?:opus|sonnet|fable|haiku)",
    re.IGNORECASE,
)

# 1.1 inventory. A row in tests/coverage.md must contain the id.
REQUIRED_COVERAGE = [
    "unit:interview",
    "unit:capture",
    "unit:reconstruction",
    "unit:check-in",
    "unit:event-logger",
    "unit:research",
    "unit:questions",
    "unit:prep-sheet",
    "unit:interval-summary",
    "unit:debrief",
    "unit:paperwork",
    "unit:bridge",
    "unit:express-prep",
    "unit:regimen-chart",
    "unit:catch-up",
    "unit:handoff",
    "twin:capabilities",
    "twin:sweep",
    "twin:freshness",
    "twin:wrapup",
    "string:tier-labels",
    "string:framing",
    "string:source-line",
    "string:handoff-why",
    "string:sync-block",
    "string:allergy-line",
    "string:record-headers",
    "string:canon-trap",
    "string:canon-distress",
    "gate:pre-share",
    "gate:alias",
    "gate:identifier-strip",
    "gate:id-number",
    "gate:caregiver-consent",
    "gate:anecdote-toggle",
    "gate:provenance-naming",
    "gate:urgent-cadence",
    "gate:capture-weave",
    "gate:paywall",
    "gate:never-transmit",
    "gate:decline",
    "gate:no-internal-labels",
    "tool:dashboard-sync",
    "tool:dashboard-censor",
    "tool:dashboard-scrub",
    "tool:dashboard-backup",
    "tool:site-censor",
    "tool:site-form",
    "tool:starter",
]

FIXED_STRINGS = [
    "מקורות רשמיים",
    "פרסומים מדעיים",
    "דיווחי מטופלים",
    "המסמך הזה נועד לתמוך בשיחה עם הצוות המטפל, לא להחליף אותה ולא להוביל לפעולה בעצמו.",
    "המקור קיים ואמר זאת נכון ל־[תאריך]. אין בכך קביעה שהדבר נכון רפואית.",
    "שום דבר לא הולך לאיבוד, כי הרשומות שלך בקבצים ולא בשיחה.",
    "◇ עדכון מהשיחה · DD.MM.YYYY",
    "אלרגיות:",
    # Old forms, declared equivalent, must remain in the file.
    "המסמך הזה נועד לתמוך בשיחה עם הצוות המטפל — לא להחליף אותה ולא להוביל לפעולה בעצמו.",
    "אין בכך קביעה שהדבר נכון רפואית.",
]

# Patient-facing surfaces. Contributor history and published demo transcripts
# are excluded on purpose; see tests/README.md.
SCAN_DIRS = [
    ROOT / "package" / "skills",
    ROOT / "package" / "references",
    ROOT / "package" / "prompts",
    ROOT / "package" / "starter",
    ROOT / "package" / "setup",
    ROOT / "package" / "web",
    ROOT / "docs" / "download",
    ROOT / "marketing",
]
SCAN_FILES = [
    ROOT / "package" / "core.md",
    ROOT / "package" / "README.md",
    ROOT / "package" / "CLAUDE.md",
    ROOT / "package" / "AGENTS.md",
    ROOT / "package" / "advolog-chatgpt-bundle.md",
    ROOT / "package" / "dashboard.html",
    ROOT / "README.md",
    ROOT / "README.en.md",
]
SCAN_DOCS_HTML = list((ROOT / "docs").glob("*.html"))

SKIP_NAME_PARTS = {"demo-run", "demo-run-en"}


def strip_html_comments(text: str) -> str:
    return re.sub(r"<!--.*?-->", "", text, flags=re.DOTALL)


def strip_fact_regions(text: str) -> str:
    return re.sub(
        r"<!-- facts:.*?-->.*?<!-- /facts:.*?-->",
        "",
        text,
        flags=re.DOTALL,
    )


def iter_scan_files() -> list[Path]:
    found: list[Path] = []
    for path in SCAN_FILES:
        if path.exists():
            found.append(path)
    for folder in SCAN_DIRS:
        if not folder.exists():
            continue
        for path in folder.rglob("*"):
            if path.is_file() and path.suffix in {".md", ".html", ".txt"}:
                found.append(path)
    for path in SCAN_DOCS_HTML:
        found.append(path)
    # unique, stable
    uniq = []
    seen = set()
    for path in found:
        if path in seen:
            continue
        if any(part in SKIP_NAME_PARTS for part in path.parts):
            continue
        seen.add(path)
        uniq.append(path)
    return uniq


def check_emdashes(errors: list[str]) -> None:
    for path in iter_scan_files():
        # platform-facts is internal bookkeeping, still patient-adjacent.
        # Em dashes are not allowed there either.
        text = path.read_text(encoding="utf-8")
        visible = strip_html_comments(text)
        for n, line in enumerate(visible.splitlines(), 1):
            if "emdash-keep" in line:
                continue
            if EM in line:
                rel = path.relative_to(ROOT)
                errors.append(f"em dash in {rel}:{n}")


def check_spans(errors: list[str]) -> None:
    for path in SCAN_DOCS_HTML:
        text = path.read_text(encoding="utf-8")
        he = len(re.findall(r'class="he"', text))
        en = len(re.findall(r'class="en"', text))
        if he != en:
            errors.append(
                f"he/en span mismatch in {path.relative_to(ROOT)}: he={he} en={en}"
            )


def check_fixed_strings(errors: list[str]) -> None:
    text = (ROOT / "package" / "references" / "report-templates.md").read_text(
        encoding="utf-8"
    )
    for s in FIXED_STRINGS:
        if s not in text:
            errors.append(f"fixed string missing from report-templates.md: {s[:48]}")
    core = (ROOT / "package" / "core.md").read_text(encoding="utf-8")
    if "מקורות רשמיים · פרסומים מדעיים · דיווחי מטופלים" not in core:
        errors.append("tier labels missing from core.md")


def check_model_names(errors: list[str]) -> None:
    allowed = ROOT / "package" / "setup" / "platform-facts.md"
    for path in iter_scan_files():
        if path.resolve() == allowed.resolve():
            continue
        text = strip_html_comments(strip_fact_regions(path.read_text(encoding="utf-8")))
        if MODEL_RE.search(text):
            errors.append(f"model name outside platform-facts.md: {path.relative_to(ROOT)}")


def check_coverage(errors: list[str]) -> None:
    path = ROOT / "tests" / "coverage.md"
    if not path.exists():
        errors.append("tests/coverage.md is missing")
        return
    text = path.read_text(encoding="utf-8")
    for item in REQUIRED_COVERAGE:
        if item not in text:
            errors.append(f"coverage row missing: {item}")


CHOSEN_DOCTOR_HE = "זמן המתנה לרופא לפי בחירת המטופל"
CHOSEN_DOCTOR_EN = "the doctor the patient chose"


def _wait_graphic_files() -> list[Path]:
    found: list[Path] = []
    why = ROOT / "docs" / "why.html"
    if why.exists():
        found.append(why)
    graphics = ROOT / "marketing" / "graphics"
    if graphics.exists():
        for path in graphics.rglob("*"):
            if path.is_file() and path.suffix.lower() in {".html", ".svg", ".md"}:
                found.append(path)
    return found


def check_why(errors: list[str]) -> None:
    page = ROOT / "docs" / "why.html"
    sources = (ROOT / "marketing" / "sources.md").read_text(encoding="utf-8")
    if page.exists():
        text = page.read_text(encoding="utf-8")
        ids = re.findall(r'data-stat="(D\d+)"', text)
        for sid in ids:
            if sid not in sources:
                errors.append(f"docs/why.html cites {sid} with no row in marketing/sources.md")
    for path in _wait_graphic_files():
        text = path.read_text(encoding="utf-8")
        if not re.search(r"\bD33\b|\bD34\b", text):
            continue
        name = path.name.lower()
        he_only = ("-he" in name or "_he" in name) and "-en" not in name and "_en" not in name
        en_only = ("-en" in name or "_en" in name) and "-he" not in name and "_he" not in name
        rel = path.relative_to(ROOT)
        if not en_only and CHOSEN_DOCTOR_HE not in text:
            errors.append(
                f"{rel} uses D33 or D34 but does not say {CHOSEN_DOCTOR_HE} on its face"
            )
        if not he_only and CHOSEN_DOCTOR_EN not in text:
            errors.append(
                f"{rel} uses D33 or D34 but does not say {CHOSEN_DOCTOR_EN!r} on its face"
            )


def _link_target(path: Path, href: str) -> Path | None:
    href = href.split("#", 1)[0].strip()
    if not href or href.startswith(("http://", "https://", "mailto:", "tel:", "data:")):
        return None
    if href.startswith("/"):
        return None
    return (path.parent / href).resolve()


def check_links(errors: list[str]) -> None:
    href_re = re.compile(r'(?:href|src)="([^"]+)"')
    pages = list((ROOT / "docs").glob("*.html"))
    pages += list((ROOT / "package").glob("*.html"))
    for path in pages:
        text = path.read_text(encoding="utf-8")
        for href in href_re.findall(text):
            target = _link_target(path, href)
            if target is None:
                continue
            if not target.exists():
                errors.append(
                    f"dead link in {path.relative_to(ROOT)}: {href}"
                )
        for repo in re.findall(r'data-repo="([^"]*)"', text):
            if "/blob/main/" not in repo:
                continue
            rel = repo.split("/blob/main/", 1)[1].lstrip("/")
            if rel and not (ROOT / rel).exists():
                errors.append(
                    f"dead data-repo in {path.relative_to(ROOT)}: {repo}"
                )


def check_generated(errors: list[str]) -> None:
    expected = build.planned_outputs()
    for rel, text in expected.items():
        path = ROOT / rel
        if not path.exists():
            errors.append(f"generated file missing: {rel} (run tools/build.py)")
            continue
        actual = path.read_text(encoding="utf-8")
        if actual != text:
            errors.append(f"generated file drifted: {rel} (run tools/build.py)")
    # Zips: every member we would write is present with the same bytes.
    # Compare by rebuilding member lists, not by hashing the zip container,
    # so a different compressor version does not fail the check.
    specs = [
        (ROOT / "docs" / "advolog.zip", build.package_zip_members()),
        (ROOT / "docs" / "advolog-skills.zip", build.skill_zip_members()),
        (ROOT / "docs" / "advolog-skill.zip", build.one_skill_zip_members()),
    ]
    for path, members in specs:
        if not path.exists():
            errors.append(f"zip missing: {path.relative_to(ROOT)}")
            continue
        with zipfile.ZipFile(path) as zf:
            names = set(zf.namelist())
            for arc, data in members:
                if arc not in names:
                    errors.append(f"{path.name} missing {arc}")
                    continue
                if zf.read(arc) != data:
                    errors.append(f"{path.name} drifted: {arc}")


def check_paste_limits(errors: list[str]) -> None:
    """7,000 is Heela's cap for the Instructions paste. T1 still confirms the live field holds it.
    OpenAI publishes no official limit. 10,000 is the verified chat-paste attachment threshold."""
    core = (ROOT / "package" / "core.md").read_text(encoding="utf-8")
    if len(core) > 7000:
        errors.append(
            f"constitution is {len(core)} characters; the Instructions cap is 7000"
        )
    instructions = ROOT / "package" / "web" / "instructions.md"
    if instructions.exists():
        n = len(instructions.read_text(encoding="utf-8"))
        if n > 7000:
            errors.append(f"instructions paste is {n} characters; the cap is 7000")
    starter_path = ROOT / "package" / "starter" / "starter-prompt.md"
    starter = starter_path.read_text(encoding="utf-8")
    if len(starter) > 10000:
        errors.append(
            f"starter file is {len(starter)} characters; a ChatGPT paste over 10000 becomes an attachment"
        )
    setup_path = ROOT / "package" / "prompts" / "setup-from-repo.md"
    setup = setup_path.read_text(encoding="utf-8")
    setup_blocks = [p for i, p in enumerate(setup.split("```")) if i % 2 == 1]
    if len(setup_blocks) < 2:
        errors.append("setup-from-repo.md needs a Hebrew block and an English block")
    for i, block in enumerate(setup_blocks):
        n = len(block.strip("\n"))
        if n > 10000:
            errors.append(f"setup prompt block {i} is {n} characters; cap is 10000")
    joined = "\n".join(setup_blocks)
    for needle in (
        "https://github.com/heelago/Advolog",
        "README.md",
        "core.md",
        "yes",
        "כן",
    ):
        if needle not in joined and needle not in setup:
            errors.append(f"setup prompt is missing {needle}")
    if "Do not send" not in setup or "אל תשלחי" not in setup:
        errors.append("setup prompt must say nothing is sent")
    if "{{ADVOLOG_RELEASE_REF}}" not in setup:
        errors.append("setup prompt must keep the {{ADVOLOG_RELEASE_REF}} placeholder")
    for needle in (
        "web/instructions.md",
        "my-record.md",
        "החבילה הציבורית",
        "public package",
        "הנחיות הפרויקט",
        "Project instructions",
        "ההקמה הכי מתאימה",
        "best available setup",
        "יש רק כן אחד",
        "There is only one yes",
        "חוט צד",
        "side thread",
    ):
        if needle not in setup:
            errors.append(f"setup prompt is missing {needle}")
    resolved = ROOT / "package" / "web" / "setup-from-repo.md"
    if not resolved.exists():
        errors.append("package/web/setup-from-repo.md was not generated")
    else:
        body = resolved.read_text(encoding="utf-8")
        if "{{ADVOLOG_RELEASE_REF}}" in body:
            errors.append("generated setup prompt still has the placeholder")
        for needle in (
            "blob/v1.2.0/README.md",
            "blob/v1.2.0/package/core.md",
            "raw.githubusercontent.com/heelago/Advolog/v1.2.0/README.md",
            "raw.githubusercontent.com/heelago/Advolog/v1.2.0/package/core.md",
        ):
            if needle not in body:
                errors.append(f"generated setup prompt is missing {needle}")
    index = (ROOT / "docs" / "index.html").read_text(encoding="utf-8")
    if "{{ADVOLOG_RELEASE_REF}}" in index:
        errors.append("docs/index.html still has the release placeholder")
    if "blob/v1.2.0/package/core.md" not in index:
        errors.append("docs/index.html does not pin the release tag")
    draft = ROOT / "tests" / "setup-prompt-draft.md"
    if not draft.exists():
        errors.append("tests/setup-prompt-draft.md is missing")
    else:
        draft_text = draft.read_text(encoding="utf-8")
        for needle in ("בדיקה בלבד", "test only", "tree/"):
            if needle not in draft_text:
                errors.append(f"draft test prompt is missing {needle}")
        pinned = re.search(r"Pinned commit: ([0-9a-f]{40})", draft_text)
        if not pinned:
            errors.append("draft test prompt needs a pinned 40-character commit")
        else:
            sha = pinned.group(1)
            for needle in (
                f"blob/{sha}/README.md",
                f"blob/{sha}/package/core.md",
                f"tree/{sha}/package",
                f"raw.githubusercontent.com/heelago/Advolog/{sha}/README.md",
                f"raw.githubusercontent.com/heelago/Advolog/{sha}/package/core.md",
            ):
                if needle not in draft_text:
                    errors.append(f"draft test prompt is missing {needle}")
        if "COMMIT_SHA" in draft_text or "/blob/main/" in draft_text:
            errors.append("draft test prompt must not point at main or a placeholder")
    walk = ROOT / "tests" / "two-chat-caregiver.md"
    if not walk.exists():
        errors.append("tests/two-chat-caregiver.md is missing")
    else:
        walk_text = walk.read_text(encoding="utf-8")
        for needle in ("דנה", "Dana", "ChatGPT", "Claude", "כן", "my-record.md"):
            if needle not in walk_text:
                errors.append(f"two-chat test is missing {needle}")
    blocks = [p for i, p in enumerate(starter.split("```")) if i % 2 == 1]
    for i, block in enumerate(blocks):
        n = len(block.strip("\n"))
        if n > 10000:
            errors.append(f"starter block {i} is {n} characters; cap is 10000")
    # Do not ship one paste that joins the starter and the constitution.
    web = ROOT / "package" / "web"
    if web.exists():
        for path in web.glob("*.md"):
            text = path.read_text(encoding="utf-8")
            if "את/ה מלווה זהיר/ה" in text and "## 10. Walls" in text:
                errors.append(
                    f"{path.relative_to(ROOT)} pastes the starter and the constitution together"
                )


def check_single_file_headers(errors: list[str]) -> None:
    records = (ROOT / "package" / "references" / "records.md").read_text(encoding="utf-8")
    for title in [
        "## הפרופיל שלי",
        "## תרופות",
        "## ציר הזמן",
        "## יומן תסמינים",
        "## שאלות פתוחות",
        "## ממצאים מאנשי מקצוע",
        "## תיבת קליטה",
    ]:
        if title not in records:
            errors.append(f"single-file section missing from records.md: {title}")


def main() -> int:
    errors: list[str] = []
    check_emdashes(errors)
    check_spans(errors)
    check_fixed_strings(errors)
    check_model_names(errors)
    check_coverage(errors)
    check_why(errors)
    check_links(errors)
    check_generated(errors)
    check_single_file_headers(errors)
    check_paste_limits(errors)
    if errors:
        print(f"{len(errors)} check(s) failed:")
        for err in errors:
            print(f"  - {err}")
        return 1
    print("check.py: ok")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
