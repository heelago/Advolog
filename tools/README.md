# Tools

```
python3 tools/build.py
python3 tools/check.py
```

`build.py` reads `package/core.md`, `package/skills/`, `package/references/`, and `package/prompts/`, and writes `package/web/`, the fallback bundle, `docs/download/`, and three zips. `instructions.md` is an exact copy of `core.md`, so the paste stays within Heela's 7,000-character Instructions cap. Live test T1 still confirms the field holds it.

`check.py` fails the build if that cap is exceeded, if a starter paste exceeds 10,000 characters, if a fixed Hebrew string drifts, if a model name appears outside `package/setup/platform-facts.md`, or if a 1.1 behavior has no row in `tests/coverage.md`.

A monthly facts routine is not in this version. The paste for it is `package/prompts/capabilities.md`. It would draft a note. It would not push.
