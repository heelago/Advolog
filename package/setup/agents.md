# עוזר אישי, איך בוחרים הקמה

המסגרת אחת. העוזרת מסתכלת מה באמת יש כאן, ומובילה אל ההקמה הכי מתאימה שאפשר באמת להשתמש בה. יש רק כן אחד, והוא מוריד את החבילה הציבורית. לא שולחים דבר. הרשומה היא קבצים, בשם `my-record.md`, לא הזיכרון ולא היסטוריית השיחה.

הסדר: אם יש גישה לתיקייה, זו הדרך. אם על המסך יש פרויקט Claude, זה המשטח הראשי, והמתאם כבוי. אם השיחה היא ChatGPT, פרויקט פרטי עם זיכרון של הפרויקט בלבד. אם כבר נמצאים ב־Dot או ב־Grok Bot, נשארים שם לפי הכללים שלמטה. בלי כל אלה, שיחה רגילה עם ההנחיות הקצרות וקובץ אחד. Duet אינו מסלול: הוא זמין בארצות הברית בלבד (נבדק 11.11.2026). אם המסך שונה, המסך קובע. הצעדים המדויקים של הפרטיות בעמוד הפרטיות באתר, נבדקו 26.11.2026.

## פרויקט Claude

שיחה ראשית אחת. קבצי הפרויקט מחזיקים את `web/instructions.md`, את `web/advolog-modules.md`, ואת `my-record.md` אם הוא כבר קיים.

ביצירת הפרויקט, נבדק 26.11.2026: מכבים את `Project coordinator`. הוא דלוק כברירת מחדל. דלוק פותח פרויקט מסוג Claude Code. כבוי נותן פרויקט רגיל. חוט צד נפתח לבד רק אם המתג נשאר דלוק.

ההנחיות, נבדק 26.11.2026: על דף הפרויקט, הוספה ואז עריכה, והשדה הנחיות הפרויקט. אם המסך עדיין מראה את הנתיב מ־23.11.2026, זה הגיבוי: גלגל השיניים, הגדרות הפרויקט, לשונית הזיכרון, אותו שדה. הוספת קבצים ב־Add context. האפשרויות שנראו ב־23.11.2026: Upload files, Upload folder, Drive, New folder.

זיכרון: לכל פרויקט זיכרון משלו. `Use account memory` נצפה דלוק ב־26.11.2026 בחשבון אחד. זו תצפית, לא ניסוח רשמי של ברירת המחדל. לרשומה רפואית כדאי לשקול לכבות, כדי שפרטים לא יבואו משיחות אחרות. נושאי בריאות לא נשמרים בזיכרון כברירת מחדל, אלא אם הדליקו Include sensitive topics in memory. משאירים כבוי. קובץ זיכרון שהעוזרת כותבת, למשל `MEMORY.md`, אומר רק שההקמה נעשתה ושהרשומה ב־`my-record.md`.

סיכום חודשי, Reflect: כשהזיכרון דלוק, Claude מסכם את נושאי השיחות. הסיכומים השמורים נשארים עד שמוחקים אותם עם Delete stored reflections בעמוד Reflect. שיחות בסתר, ושיחות שמשתמשות בחיבור בריאות, לא נכנסות לסיכום. נקרא 26.11.2026: https://support.claude.com/en/articles/15672559-see-your-monthly-recap

בדיקות תקופתיות: הטקסטים ב־`prompts/` (סריקה, טריות, יכולות, יומן שבועי). איפה שהמסך מציע משימה מתוזמנת, זה הטקסט. אין חיבור לדוא"ל או לדרייב בשביל הרשומה.

פרטיות: Settings, Privacy, מכבים את Help Improve our AI models. השם על המסך יכול להיות קצת שונה. נבדק 26.11.2026.

## פרויקט ChatGPT

פרויקט פרטי. בשדה ההנחיות מדביקים את `web/instructions.md`. מעלים את קובץ המודולים. מצרפים את `my-record.md`. רק אז שיחה חדשה בתוך הפרויקט.

זיכרון של הפרויקט בלבד, נבדק 26.11.2026: שלוש הנקודות, Project settings, תחת Memory, Project-only memory. זה יכול לקחת כמה שעות. בתוך פרויקט כזה ChatGPT Work אינו זמין (נבדק 14.8.2026).

OpenAI כותבת, בדף Health in ChatGPT שנקרא ב־26.11.2026: למידע של מישהו אחר, חשבון נפרד או פרויקט נפרד עם זיכרון של הפרויקט בלבד וקבצים שהועלו. ולשיחות הבריאות, פרויקט נפרד עם אותו זיכרון. זה מתאים להקמה כאן, ולמסלול של מי שמתעדת עבור מישהו קרוב, רק בהסכמה. https://help.openai.com/en/articles/20001036-health-in-chatgpt

Health עצמו זמין בארצות הברית, לא בישראל. כשהזיכרון דלוק, שיחות שמשתמשות ב־Health יכולות ליצור זיכרונות לשיחות הבאות. הילה, 19.11.2026. לא מכניסים פרטי בריאות לזיכרון.

פרטיות: Settings, Data controls, מכבים את Improve the model for everyone. בחשבון אישי הוא דלוק כברירת מחדל. נבדק 26.11.2026.

בדיקות תקופתיות: איפה שהמסך מציע Task, הטקסט הוא אחד מקובצי `prompts/`.

## Dot

אותו מתג של ChatGPT, Improve the model for everyone, חל גם על השיחות, הפעולות, והאוטומציות של ה־dot. נקרא 26.11.2026. ל־dot זיכרון משלו, והוא נשאר דלוק גם כשמכבים את הזיכרון של ChatGPT. אי אפשר למחוק ממנו פריט אחד. מחיקת ה־dot מתחילה את מחיקת הזיכרון שלו. לא מספרים לו פרטי בריאות שלא היו רוצים שיישארו. לא מחברים תיבת דוא"ל בשביל הרשומה. ההקמה היא אותה הנחיה, ואותה חבילה.

## Grok Bot

האימון נקבע לפי הגדרות הפרטיות של חשבון Cursor. לא נמצא דף רשמי שאומר בפשטות מה קורה בחשבון אישי, ולכן לא מכניסים אליו פרטי בריאות עד תשובה ברורה מהתמיכה. אין מסך זיכרון: שואלים מה הוא זוכר, ומבקשים שישכח. איפוס שיחה לא מוחק את הזיכרון. מחיקת הבוט כן. כל הבוטים של המשתמש חולקים מחשב ענן אחד, וזה אינו גבול אבטחה. נקרא 26.11.2026: https://docs.x.ai/grok-bot/approvals-security-and-privacy

ההקמה: פותחים את תיקיית `package/` כדי ש־`AGENTS.md` ייטען, וקוראים את `core.md` קודם.

## Claude Code, או סוכן עם תיקייה כמו Codex

Claude Code קורא את `CLAUDE.md`. Codex קורא את `AGENTS.md`. שני הקבצים זהים, ושניהם שולחים אל `core.md` קודם. התיקייה היא ההקמה: הרשומה יושבת ליד החבילה, לא בתיקייה משותפת. אחרי הורדה, סוגרים ופותחים מחדש את `package/` כדי שהקובץ ייטען. בדיקות תקופתיות: קוראים את `prompts/` כשמבקשים, או שמים את הטקסט במשימה מתוזמנת אם המסך מציע אחת. אין חיבור לדוא"ל בשביל הרשומה. מתג האימון הוא של החשבון, והצעדים בעמוד הפרטיות.

## שיחה רגילה

כשאין פרויקט ואין תיקייה: מדביקים את `web/instructions.md` (עד 7,000 תווים) ומעלים קובץ אחד, `web/advolog-modules.md`. שומרים `my-record.md` בסוף. פרטי בריאות מחוץ לזיכרון. בדיקה תקופתית היא הדבקה של הפרומפט, כשרוצים.

---

# A personal agent, how to choose a setup

One framework. Look at what is actually here, and guide the person to the best setup they can use. There is only one yes, and it downloads the public package. Nothing is sent. The record is files, named `my-record.md`, not memory and not chat history.

The order: if a folder can be read, that is the path. If a Claude Project is on the screen, that is the primary surface, with the coordinator off. If the chat is ChatGPT, a private project with project-only memory. If you are already Dot or Grok Bot, stay there under the rules below. Without any of those, a plain chat with the short instructions and one file. Duet is not a path: it is available in the United States only (checked 11.11.2026). If the screen differs, the screen wins. The exact privacy steps are on the site privacy page, checked 26.11.2026.

## A Claude Project

One main chat. Project files hold `web/instructions.md`, `web/advolog-modules.md`, and `my-record.md` if it already exists.

When creating the project, checked 26.11.2026: turn `Project coordinator` off. It is on by default. On opens a Claude Code style project. Off gives a normal project. A side thread starts on its own only if the switch is left on.

Instructions, checked 26.11.2026: on the project page, Add then Edit, then the Project instructions field. If the screen still shows the 23.11.2026 path, that is the fallback: the gear, Project settings, the Memory tab, the same field. Add files with Add context. The choices seen on 23.11.2026 were Upload files, Upload folder, Drive, and New folder.

Memory: each project has its own. `Use account memory` was observed on, on one account, on 26.11.2026. That is an observation, not an official statement of the default. For a medical record, consider turning it off, so details do not come in from other chats. Health topics are not saved to memory by default, unless Include sensitive topics in memory is on. Leave that off. A memory file the assistant writes, such as `MEMORY.md`, may say only that setup is done and the record lives in `my-record.md`.

Monthly recap, Reflect: when memory is on, Claude summarizes chat topics. Stored reflections stay until they are deleted with Delete stored reflections on the Reflect page. Incognito chats, and chats that use a health integration, are left out of the recap. Read 26.11.2026: https://support.claude.com/en/articles/15672559-see-your-monthly-recap

Scheduled checkups: the texts in `prompts/` (sweep, freshness, capabilities, weekly log). Where the screen offers a scheduled task, that text is the task. Do not connect email or a drive for the record.

Privacy: Settings, Privacy, turn off Help Improve our AI models. The name on the screen may differ slightly. Checked 26.11.2026.

## A ChatGPT project

A private project. Paste `web/instructions.md` into Instructions. Upload the modules file. Attach `my-record.md`. Only then open a new chat inside the project.

Project-only memory, checked 26.11.2026: the three dots, Project settings, under Memory, Project-only memory. It may take a few hours. ChatGPT Work is not available inside that project (checked 14.8.2026).

OpenAI writes, on the Health in ChatGPT page read on 26.11.2026: for someone else's information, use a separate account or a separate project with project-only memory and uploaded files. For health chats, a separate project with that same memory. That matches this setup, and the path for keeping a record for someone close, only with consent. https://help.openai.com/en/articles/20001036-health-in-chatgpt

Health itself is available in the United States, not in Israel. When memory is on, conversations that use Health can create memories for later chats. Heela, 19.11.2026. Do not put health details into memory.

Privacy: Settings, Data controls, turn off Improve the model for everyone. On a personal account it is on by default. Checked 26.11.2026.

Scheduled checkups: where the screen offers a Task, the text is one of the files in `prompts/`.

## Dot

The same ChatGPT setting, Improve the model for everyone, also covers a dot's conversations, actions, and automations. Read 26.11.2026. A dot has its own memory, and it stays on even when ChatGPT's memory is off. A single item cannot be deleted. Deleting the dot starts deleting its memory. Do not tell it health details you would not want kept. Do not connect a mailbox for the record. Setup is the same instruction, and the same package.

## Grok Bot

Training follows the privacy settings of the Cursor account. No official page says plainly what happens on a personal account, so keep health details out of it until support gives a clear answer. There is no memory screen: ask what it remembers, and ask it to forget. Resetting a conversation does not erase memory. Deleting the Bot does. All of a user's bots share one cloud computer, and that is not a security boundary. Read 26.11.2026: https://docs.x.ai/grok-bot/approvals-security-and-privacy

Setup: open the `package/` folder so `AGENTS.md` loads, and read `core.md` first.

## Claude Code, or a folder agent such as Codex

Claude Code reads `CLAUDE.md`. Codex reads `AGENTS.md`. The two files match, and both send you to `core.md` first. The folder is the setup: the record sits beside the package, not in a shared folder. After a download, close and reopen `package/` so the file loads. Scheduled checkups: read `prompts/` when asked, or put that text in a scheduled task if the screen offers one. Do not connect email for the record. The training switch is the account's, and the steps are on the privacy page.

## A plain chat

When there is no project and no folder: paste `web/instructions.md` (at most 7,000 characters) and upload one file, `web/advolog-modules.md`. Save `my-record.md` at the end. Keep health details out of memory. A checkup is pasting the prompt, when you want it.
