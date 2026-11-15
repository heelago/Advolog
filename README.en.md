# Advolog

Advolog helps patients and caregivers walk into an appointment with one orderly page: what happened, what was tried, and which questions are worth asking. It runs inside the Claude, ChatGPT, or personal agent you already have, with no account and no server of its own. It does not diagnose, recommend treatment, or handle emergencies.

You should not have to study engineering to arrive prepared.

## How to start

Claude is the primary surface. You do not download a zip by hand.

1. Check training, memory, web access, and file creation.
2. Paste the Hebrew block in `package/prompts/setup-from-repo.md`. The assistant reads the README, explains, and asks whether to download. Only a yes continues. Then it reads `core.md`.

If there is no web access or no file creation: paste `package/core.md` (at most 7,000 characters) and upload `package/web/advolog-modules.md`. The zip remains a fallback for a folder you already download by hand.

Details, including counts that have not yet been measured on a live run: [`docs/start.html`](docs/start.html).

## What you can ask

In ordinary words: a page for tomorrow's visit, questions with a reason, a line about what hurts, a place to drop things when organizing is too much, a letter from the health fund, the story for a new doctor, a catch-up after a gap. The list: [`docs/gallery.html`](docs/gallery.html).

## The principles that do not bend

- Questions, never advice: no diagnosis, no treatment recommendation, no dose.
- Evidence tiers always labeled, never blended: **Official sources · Scientific publications · Patient reports**.
- No invented citation. What cannot be verified is dropped, out loud.
- In distress: real resources (in Israel: 101, ERAN 1201, Sahar), no methods, no alarm.
- The user decides, and the tool never sends anything.

## Privacy

Three lines: nothing reaches us. Conversations stay with the company you already use. The toolkit adds habits, not a promise of secrecy. [The full page](docs/privacy.html).

## About the developer

Advolog was built by Dr. Heela Goren. Through [h2eapps](https://h2eapps.com/about) she builds open tools that work without technical expertise and without replacing human judgment.

## License

MIT (`LICENSE`). This tool is not medical advice.

Version 1.2.0 (11.11.2026). What changed: [`CHANGELOG.md`](CHANGELOG.md). Hebrew: [`README.md`](README.md).
