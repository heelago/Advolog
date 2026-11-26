# Advolog

Advolog helps patients and caregivers walk into an appointment with one orderly page: what happened, what was tried, and which questions are worth asking. It is a package, not a site and not a wrapper: nothing passes through us, and the same package opens wherever permissions are already given. Whichever way you open it, your assistant guides you to the best available setup. It runs inside the Claude, ChatGPT, or personal agent you already have, with no account and no server of its own. It does not diagnose, recommend treatment, or handle emergencies.

You should not have to study engineering to arrive prepared.

## How to start

Claude is the primary surface. Check whether you have a Claude Project: one main conversation, and it starts the side work. One long session gets heavy. If the screen still shows a project with an Instructions field, that still works. You do not download a zip by hand.

1. Check training, memory, web access, and file creation.
2. Paste the Hebrew block in `package/prompts/setup-from-repo.md`. The assistant reads the README, explains, says what the account has, and asks for one yes. Only that yes downloads the public package. Then the instructions are saved where the chosen setup keeps them.

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

## Credits

Advolog was not built in a vacuum. These are the works it draws on, and a few more worth knowing.

**Advolog draws on**

- [Kol Zchut](https://www.kolzchut.org.il/en/Main_Page): the free database of the rights of Israeli residents and how to exercise them. Its pages are the source for Advolog's Israel layer, for example drugs outside the basket and private health insurance.
- [Ask Me 3](https://www.ihi.org/resources/tools/ask-me-3-good-questions-your-good-health), Institute for Healthcare Improvement: three questions for every visit. They are the floor of the prep sheet when there is hardly any record yet.
- [QuestionBuilder](https://www.ahrq.gov/questions/question-builder/index.html), AHRQ: a free app for preparing questions before a visit, where what you enter stays on your device. The idea of a question you can rehearse comes from there.
- [Patients Use AI](https://patientsuseai.substack.com/), Dave deBronkart: patient-led writing on using AI with the health system. The idea of a list of plain, proven requests on the "What you can ask" page comes from there.
- [Agent Skills](https://agentskills.io/specification): an open format for AI assistant capabilities. Advolog's skills are written in it.

**Similar work worth knowing**

- [Israel Patients' Rights Association](https://www.patients-rights.org/): a nonprofit that gives information on medical rights and takes requests for help. When you need a person, not a tool.
- [CareGivers Israel](https://www.caregivers.org.il/): the organization for family caregivers, with information, counseling and personal guidance. Related to Advolog's path for keeping a record for someone close.
- [Open Notes Labs](https://www.opennotes.org/): an academic lab studying what happens when patients read their own records. The same belief: people who read their record understand more and catch errors.
- [AI Rights for Patients](https://lightcollective.org/2024/04/08/advocacy-leaders-publish-first-of-its-kind-governance-framework-for-artificial-intelligence-ai-rights-for-patients/), Light Collective: a governance framework for AI in health, written by patients.
- [Society for Participatory Medicine](https://participatorymedicine.org/): a community promoting partnership between patients, caregivers and health professionals.
- [Fight Health Insurance](https://fighthealthinsurance.com/) ([code](https://github.com/fighthealthinsurance/fighthealthinsurance)): a free tool that drafts appeals of US health insurance denials. The same principle: the AI drafts, you decide and send.
- [Fasten](https://github.com/fastenhealth/fasten-onprem): an open-source, self-hosted personal and family medical record manager. The repository is archived. Advolog chose plain text files over system integrations.
- [medical-appointment-advocate](https://github.com/mohitagw15856/pm-claude-skills/blob/main/skills/medical-appointment-advocate/SKILL.md): an open skill, in the same format, for preparing for a doctor's appointment, for yourself or someone you care for.

Know of work that belongs here? Tell us on GitHub.

## License

MIT (`LICENSE`). This tool is not medical advice.

Version 1.2.0 (11.11.2026). What changed: [`CHANGELOG.md`](CHANGELOG.md). Hebrew: [`README.md`](README.md).
