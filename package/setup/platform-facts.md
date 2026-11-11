# Platform facts

<!-- The only file that may name a model. Checked 2026-11-11 by a second reader
     against the vendors' own pages. Rows marked "needs live test" stay pending
     until Heela runs them in her own accounts. Guides do not repeat model names.
     The 7,000-character Instructions cap is Heela's rule. Live test T1 still
     confirms the field holds it. OpenAI publishes no official limit. -->

**Version:** 1.2.0 · checked 2026-11-11.

**Pending, because they need a live test:** G5 (Instructions field size; no official number), G8 (whether project files are read in full or searched), C4's confirmation that our modules do not trigger project RAG (T3), C2's multi-folder zip (T4), and T5, T6, T7. Steps are at the end of this file.

**Instructions cap, approved by Heela (11.11.2026):** the constitution paste is at most 7,000 characters, Hebrew included. This is the repo rule. OpenAI publishes no official limit. Live test T1 still confirms that the field holds a 7,000-character paste. Do not raise the cap before that. A ChatGPT chat paste over 10,000 characters becomes an attachment on every plan (G7, verified). The starter is one language block, not the constitution plus the starter.

Decision 19 stands: Claude web uses project knowledge, not an account-level skill. Decision 20 stands: the upload is one skill folder. The twelve-skill zip is the repo tree and a folder install, not the documented upload.

The tables below are the second-reader check, kept as written.

---

# Advolog platform facts: Phase 0 check

Checked 2026-11-11 (Asia/Jerusalem) by Grok Bot as second reader. Each fact was read today on the vendor's own page unless the row says otherwise. Help pages change often: anything that ships in a guide should be re-read in the week of the merge.

Status key:
- **verified**: stated on an official page opened today.
- **corrected**: the brief or the repo said something different; the official page wins.
- **not stated**: the official pages are silent; only third parties give a number.
- **needs live test**: only a test in Heela's own accounts can settle it. Steps are in the last section.

Some vendor pages (openai.com, help.openai.com, oecd.org) return 403 to scripts but open normally in a reader. That is a bot block, not a dead link.

## Claude (Anthropic)

| # | Fact | Status | Source | Date on source | Effect on Advolog |
|---|---|---|---|---|---|
| C1 | Skills are available on Free, Pro, Max, Ultra, Team and Enterprise, and require "Code execution and file creation" (called "Create and edit files" in the new settings layout) to be on | verified | https://support.claude.com/en/articles/12512180-use-skills-in-claude | Page "updated today" | Guide step 1 for Claude must tell the user to switch that setting on first. |
| C2 | Upload path: Customize > Skills > + > Create skill > Upload a skill > "Upload a ZIP file containing your skill folder" (singular). Listed upload errors include "Skill folder name doesn't match the skill name". Best practice on the page: "Create separate skills for different purposes" | verified | Same as C1 | Same | **Decision 20.** A ZIP with many skill folders is not documented anywhere. The default (a), one router skill with modules as reference files, is the documented path. Multi-folder ZIP: needs live test (T4). |
| C3 | Skills sync to Claude Code from version 2.1.273 | verified | Same as C1 | Same | Heela's laptop runs 2.1.309, so sync works. |
| C4 | Project knowledge RAG is on paid plans only (Pro, Max, Ultra, Team, Enterprise). It turns on automatically "when your project knowledge approaches the context window limit". No numeric threshold is published. When on, a visual indicator shows, and Claude uses a "project knowledge search" tool. On Free, project capacity is simply the context window | verified (threshold not stated) | https://support.claude.com/en/articles/11473015 | Opened today | **Decision 19 supported.** The modules bundle measured today is 109,104 bytes / 93,160 characters in full; the module set alone is about 67 KB, about 57,000 characters, mostly English, roughly 15,000 to 20,000 tokens. That is far below any Claude context window, so it should load in full. Confirm with T3. |
| C5 | Claude Docs is on Free, Pro, Max, Ultra, Team and Enterprise, on by default (Enterprise turned on by default from 15 Oct 2026). Free plans cannot send share invitations | verified | https://support.claude.com/en/articles/16923645-get-started-with-claude-docs | Opened today | Decision 35 (Docs over Motion) stands. Note for guides: a Free user can share by link, not by invitation. |
| C6 | Claude Motion is a beta on Team and Enterprise only. Docs, Slides and Design are out of beta on every plan, Free included. Standalone claude.ai/design closes on 14 December | verified | https://claude.com/resources/articles/dashboards-and-motion | Opened today | Decision 35 stands: no Motion in the patient path. |
| C7 | Fable 5.2 and Mythos 5.2 announced 9 November 2026: up to 30% faster than 5.1, USD 8 / 40 per million input / output tokens | verified | https://www.anthropic.com/claude-fable-and-mythos-5-2 | 9 Nov 2026 | None for patients. |
| C8 | Fable plan access: Fable 5.2, 5.1 and 5 on all paid plans, not Free. Max, Ultra and premium seats: up to 50% of weekly limits. Pro and standard Team seats: usage credits. Claude Code minimum versions: Fable 5.2 needs 2.1.321, 5.1 needs 2.1.255, 5 needs 2.1.170 | verified | https://support.claude.com/en/articles/15424964-claude-fable-models-on-your-plan | Opened today | Advolog must never require Fable. **Heela's laptop (2.1.309) cannot use Fable 5.2 in Claude Code until it is updated** (T7). |
| C9 | Opus 5.5 released 22 Sep 2026: performs at about Fable 5.1 level for about 40% less; default effort medium; "no longer available with thinking mode switched off"; more resistant to prompt injection | verified | Opus 5.5 "what's new" page on platform.claude.com (resolves, 200) | 22 Sep 2026 | Guides must not tell Claude users to switch thinking off. |
| C10 | Claude Duet: research preview, US only, Pro, Max and Ultra by waitlist. Runs on Opus 5.5 with no model choice. Asks before sending, paying, signing or deleting. Reads the user's memory, skills and connectors | verified | https://support.claude.com/en/articles/17631495-get-started-with-claude-duet | Opened today | Not available to Israeli users. Leave out of Hebrew guides. |
| C11 | Fable 5 prompting guide: "Skills developed for prior models are often too prescriptive for Claude Fable 5 and can degrade output quality"; Fable 5 runs safety classifiers on offensive cyber, biology and life sciences content | verified | https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-fable-5 | Opened today | Supports the brief's "shorter, less prescriptive modules" item. The biology classifier is worth knowing: if a patient's medical text trips it, Fable may refuse. Mention only in the builder notes, not in patient copy. |
| C12 | Opus 5 prompting guide: "Claude Opus 5 verifies its own work without being told to. If your prompt contains explicit verification instructions ... remove them: instructions like these cause over-verification". Context window 1M tokens, default and maximum | verified | https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-opus-5 | Opened today | Supports removing "check your work" lines from module text. |

## ChatGPT (OpenAI)

| # | Fact | Status | Source | Date on source | Effect on Advolog |
|---|---|---|---|---|---|
| G1 | Chat runs GPT-6 since 7 Oct 2026: GPT-6 Sol on Plus, Pro, Business and Enterprise; GPT-6 Luna on Free and Go (from 8 Oct). Reasoning options run from Instant through Extra High. The Pro option uses GPT-6 Astra | verified | https://help.openai.com/en/articles/6825453-chatgpt-release-notes (7 Oct entry) | 7 Oct 2026 | Repo guides that name "GPT-5.6 Luna" are out of date. Decision 9 (no model names in patient copy) protects against the next change. |
| G2 | GPT-6.1 Sol (29 Sep 2026) and GPT-6.1 Terra (26 Oct 2026) run in ChatGPT Work and Codex only, on Plus, Pro, Business, Enterprise and Edu. Not in Chat | verified | Release notes, 29 Sep and 26 Oct entries; https://help.openai.com/en/articles/20001275-chatgpt-work-and-codex | 29 Sep, 26 Oct 2026 | No change to the plan. |
| G3 | Naming trap: on 22 Sep OpenAI added "GPT-6 Sol and GPT-6 Luna in Work and Codex. These models are separate from the models available in Chat" | verified | Release notes, 22 Sep entry | 22 Sep 2026 | Same names, different models. Another reason for decision 9. |
| G4 | Free and Go have a Think button on the web (since 14 Aug 2026). Plus and Pro no longer auto-switch from Instant to Thinking (14 Sep 2026) | verified | Release notes, 14 Aug and 14 Sep entries | Aug to Sep 2026 | **Small correction to the brief:** the old guides' "Think" option is not wrong for Free and Go on the web; it is the right word there. "Choose Instant" is still stale for paid plans, where the picker now shows reasoning levels. |
| G5 | Project Instructions field: **no character limit is stated** on any official page opened today (Projects help, release notes). Third parties (Elephas, a Reddit report of 26 Sep 2026) say 8,000 characters; a Japanese write-up of 4 Oct 2026 found no official figure | not stated, needs live test | Projects help on help.openai.com; third-party pages as named | Opened today | **Risk for decision 17.** The planned constitution of about 8 KB, mostly English, is about 8,000 characters: right at the reported limit. Heela approved a repo cap of 7,000 characters, Hebrew included (11.11.2026). T1 still confirms the live field holds it. |
| G6 | Global custom instructions (not project Instructions): 5,000 characters on Plus, Pro, Business, Enterprise and Education since 15 Jul 2026 (up from 1,500). Free and Go remain at 1,500 | verified | Release notes, 15 Jul entry | 15 Jul 2026 | Do not confuse with G5. Not used by Advolog. |
| G7 | Pasting more than 10,000 characters into the chat composer turns the paste into an attachment, on all plans. The user can click "Show in text field" to turn it back | verified | Release notes, 22 Jun and 4 Aug entries | Jun to Aug 2026 | **Affects option C ("starter plus") in the guides:** any starter paste longer than 10,000 characters arrives as a file, not as message text. Keep any paste under 10,000 characters, or tell the user what they will see. |
| G8 | Project files: whether ChatGPT searches them or loads them in full is **not stated**. The upload help says only that "Files saved as GPT knowledge or project files are handled differently from direct chat attachments" | not stated, needs live test | File uploads FAQ on help.openai.com | Opened today | Decision 17's design (the rules that must always apply live in Instructions; modules live in files) is safe either way. T2 tells us whether a rule placed only in a file is reliably followed. |
| G9 | Project file limits: Free 5 files per project, Go and Plus 25, Pro, Business, Enterprise and Edu 40. Up to 10 files at once. Free users: 3 uploads a day. Text files up to 2M tokens each | verified | File uploads FAQ and Projects help on help.openai.com | Opened today | The Free 5-file limit and 3 uploads a day matter: the Free path must use five files or fewer, uploaded on one day only if three or fewer. |
| G10 | A project's memory setting can now be changed after creation (Default or Project-only). Shared projects stay project-only. **"ChatGPT Work is not available in projects using project-only memory."** | verified | Release notes, 14 Aug entry | 14 Aug 2026 | New. If the guide recommends project-only memory (privacy), the user loses Work inside that project. Say so in one line; it is a fair trade for patients. |
| G11 | Custom GPTs retire on 11 Dec 2026 (FedRAMP and approved-deferral workspaces: 11 Feb 2027) and migrate to plugins | verified | https://help.openai.com/en/articles/20001519 and release notes, 11 Sep entry | Sep 2026 | Advolog must not offer a Custom GPT. Decision unchanged. |
| G12 | Personal Skills are generally available only on Business, Enterprise, Healthcare and Edu. Plugins can bundle skills; Plugin Creator exists; plugin ZIP upload is in the admin console only | verified | Skills and plugins help pages on help.openai.com; release notes, 9 Jul entry | Jul to Oct 2026 | The consumer ChatGPT path stays "project Instructions plus files" (decision 17 unchanged). A personal-plugin route is an idea only (T6). |
| G13 | Health in ChatGPT: US only, 18 and older, Free to Pro | verified | Release notes, 23 Jul entry | 23 Jul 2026 | Not available to Israeli users; do not mention it in Hebrew guides. |
| G14 | Data controls FAQ (training opt-out wording) | not re-read | https://help.openai.com/en/articles/7730893-data-controls-faq (403 to scripts) | n/a | Re-read in a browser before the privacy line in the guide ships. |
| G15 | OpenAI's GPT-6 prompting guide | not re-read | https://openai.com/index/practical-guide-building-gpt-6/ (403 to scripts) | n/a | Re-read in a browser if module text relies on it. |

## Other URLs from the brief and addendum

Resolved today (HTTP 200): Fable 5 and Opus 5 prompting guides, Opus 5.5 "what's new", Fable 5.2 pages, OpenAI skills blog, gpt-6.1-sol model page, agentskills.io spec, Claude Docs help, Claude memory help, Claude privacy page, GitHub Pages limits, YouTube privacy-enhanced (nocookie) help, HyperFrames repo and skills guide, Remotion skills pages, ivrit.ai, apiyi, modellix. Their content was not re-read in this pass except where a row above says so.

## Live tests Heela needs to run

Use a fresh test project each time and delete it afterwards. None of these tests sends anything to anyone. Write the result into this file under the test.

**T1. ChatGPT project Instructions size limit (decision 17).** On Plus, and on Free if you have a Free account:
1. Make three plain-text blocks of exactly 7,000, 8,000 and 9,000 characters. Each one ends with a unique last line, for example `END-7000`, `END-8000`, `END-9000`. (Ask me and I will generate them; mix in about 1,000 Hebrew characters so the test is realistic.)
2. New project > project settings > Instructions. Paste the 7,000 block, save, close, reopen, and check the last line is still there.
3. Repeat with 8,000 and 9,000.
4. Record: the largest block that saves whole; whether a too-long block is refused or silently cut.

**T2. ChatGPT project files, full load or search (decision 17).**
1. Make one text file of about 60 KB with three made-up code words placed at about 10%, 50% and 90% of the file, for example `canary-alef`, `canary-bet`, `canary-gimel`, each in a normal sentence.
2. Upload it as a project file. Leave Instructions empty.
3. In a new chat in the project, ask: "List every word that starts with canary in the project files, verbatim, and say where each appears."
4. In another new chat, ask an unrelated question first, then: "Without searching, what is the code word in the middle of the file?"
5. Record: how many of the three it finds, and whether a "searched files" or similar indicator appears.

**T3. Claude project knowledge loads in full (decision 19).** On Pro (and Free if available):
1. Upload the real module bundle (about 67 KB) plus the same canary sentences to a new project.
2. Look at the project knowledge panel for the RAG indicator.
3. Ask the same canary questions as T2 and watch for a "project knowledge search" tool call in the reply.
4. Record: indicator yes or no; tool call yes or no; canaries found.

**T4. Claude "Upload a skill" with two skill folders in one ZIP (decision 20).**
1. Make a ZIP containing two folders, `test-a/SKILL.md` and `test-b/SKILL.md`, each with a valid name and description matching its folder.
2. Customize > Skills > + > Create skill > Upload a skill, and upload it.
3. Record: rejected (and the exact error), only one skill created, or both created.
4. Then upload a ZIP with one folder holding `SKILL.md` and a `references/` folder, and confirm it works. This is the default (a) layout.

**T5. Skills need code execution (guide wording).**
1. Settings > Capabilities: switch "Code execution and file creation" (or "Create and edit files") off.
2. Open Customize > Skills and record what the page shows. Switch it back on.

**T6 (optional). Plugin Creator on a personal plan.** On Plus, open the Plugins area and record whether Plugin Creator or "create plugin" is offered. Only an idea for later; no decision depends on it.

**T7 (optional, your laptop). Update Claude Code.** Run `claude update` (or your usual update method), then `claude --version` should show 2.1.321 or later, and `/model` should list Fable 5.2. This changes your laptop, so it is your call.
