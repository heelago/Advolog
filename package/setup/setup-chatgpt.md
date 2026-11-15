# התקנה ב־ChatGPT

המשטח הראשי של Anthropic הוא Claude. כאן המסלול כשיש ChatGPT. שמות מודלים רק בקובץ העובדות. אם המסך שונה, המסך קובע.

לא שומרים את הרשומה בפרויקט משותף. לא הופכים את הלוח לאתר שאפשר לפרסם. לא שולחים דבר.

## הדרך הראשית

אותה כמו ב־Claude, אם לשיחה יש גישה לאינטרנט ויצירת קבצים: בודקים אימון, זיכרון, אינטרנט וקבצים, ומדביקים את `prompts/setup-from-repo.md`. ההורדה רק אחרי כן.

## מסלול גיבוי, בלי אינטרנט או בלי יצירת קבצים

אומרים את זה במפורש. תקרת ההנחיות היא 7,000 תווים, כולל עברית. OpenAI לא פרסמה מספר, ובדיקה חיה T1 עוד תאשר שהשדה מחזיק את כולם. הדבקה מעל 10,000 תווים בצ'אט הופכת לקובץ מצורף. לא מדביקים את טקסט ההקמה ואת ההנחיות בהודעה אחת. אם הופיע קובץ מצורף, «Show in text field», או מדביקים את ההנחיות בשדה של הפרויקט.

1. נכנסים ל־chatgpt.com ומתחברים.
2. Projects, פרויקט חדש. שם חופשי.
3. בשדה ההנחיות מדביקים את `web/instructions.md`. באתר יש כפתור «העתקת ההנחיות». זה החלק שחל תמיד, גם אם קובץ אחר לא נשלף באותו תור.
4. בתוכנית שמאפשרת כמה העלאות ביום, מעלים את ארבעת הקבצים `web/modules-1-start.md` עד `web/modules-4-deeper.md`. בתוכנית החינמית יש 3 העלאות ביום ו־5 קבצים לפרויקט (נבדק 11.11.2026), אז מעלים קובץ אחד: `web/advolog-modules.md`. אם גם זה לא נכנס, `advolog-chatgpt-bundle.md`.
5. זיכרון ברמת הפרויקט, אם האפשרות מופיעה. זה מונע מ־ChatGPT Work לעבוד בתוך הפרויקט (נבדק 11.11.2026). לרשומה רפואית זה חילוף הוגן: הרשומה היא הקבצים, לא הזיכרון.
6. שיחה חדשה, ומתחילים לדבר.

בטלפון ובאתר שומרים בסוף השיחה קובץ אחד, `my-record.md`. שבעת הקבצים נשארים שווי ערך למי שכבר עובד איתם.

## תיקייה במחשב, או Codex

אם השיחה יכולה לקרוא את המאגר וליצור קבצים, משתמשים בהנחיית ההקמה, לא בהורדת zip ביד. Codex רשום כ«עובד לפי התיעוד הרשמי, לא הורץ אצלנו». הוא קורא את `AGENTS.md`.

## מאמץ

<!-- facts:effort -->
לכל העבודה מספיקה ברירת המחדל, איפה שהתוכנית מציעה אותה. לא מעלים מאמץ רק כי זו הכנה לביקור. המודל החזק יותר מוצע פעם אחת, להחלטה קשה, למידע סותר, או לביורוקרטיה מסובכת, והעוזרת לא מחליפה אותו לבד. השם והבורר בפסקת המודל. אם המסך שונה, המסך קובע.
<!-- /facts:effort -->

## העלאות

לפני כל העלאה חותכים או מכסים את מספר הזהות. מכתב סרוק שעולה כ־PDF עלול להגיע ריק, כי בחלק מהתוכניות נקרא רק הטקסט הדיגיטלי. אם הקובץ ריק, מבקשים צילום של העמוד. בתוכנית החינמית: 3 העלאות ביום (נבדק 11.11.2026).

דף ההכנה נשאר קובץ מלא אחד, לשמירה ולהדפסה, אלא אם השיחה באמת מציעה מסמך אחר. לא מבטיחים פורמט שלא מופיע.

## שיחה חדשה

Projects, הפרויקט, New chat, ומדביקים את פתק המסירה ראשון. «תתעדכני».

## זיכרון

<!-- facts:memory-chatgpt -->
ההמלצה: זיכרון של הפרויקט בלבד, כדי שהתיק לא יישאב מהזיכרון הכללי ולא יזין אותו. איפה המתג, ומתי השינוי נכנס לתוקף, נבדק ב־1.10.2026 וממתין לבדיקה חוזרת. אפשר גם לכבות זיכרון לגמרי. המסך קובע.
<!-- /facts:memory-chatgpt -->

## פרטיות החשבון

מבטלים שימוש בשיחות לאימון, איפה שהתוכנית מאפשרת. הצעדים המדויקים ממתינים לאימות בדף `privacy.html`.

---

# Setup in ChatGPT

Claude is the primary Anthropic surface. This is the path when the chat is ChatGPT. Model names stay in the facts file. Your screen wins.

Do not keep the record in a shared project. Do not publish the dashboard as a site. Nothing is sent.

## The primary path

The same as Claude, when the chat can open the web and create files: check training, memory, web access, and file creation, then paste `prompts/setup-from-repo.md`. The download waits for a yes.

## Fallback, when there is no web access or no file creation

Say so plainly. The instructions stay at or under 7,000 characters, Hebrew included. That cap is the rule. OpenAI publishes no number, and live test T1 still confirms the field holds it. A chat paste over 10,000 characters becomes an attachment. Do not paste the setup text and the instructions as one message. If an attachment appears, use "Show in text field", or paste the instructions into the project field.

1. Sign in at chatgpt.com.
2. New project.
3. Paste `web/instructions.md` into Instructions. The site button says "copy the instructions". This part applies on every turn, even if another file is not retrieved.
4. Where the plan allows several uploads a day, upload `web/modules-1-start.md` through `web/modules-4-deeper.md`. On the Free plan there are 3 uploads a day and 5 files per project (checked 11.11.2026), so upload one file: `web/advolog-modules.md`. If that does not fit, use `advolog-chatgpt-bundle.md`.
5. Project-only memory, if you see the option. Where it sits is pending verification. The files are the record, not the memory.
6. A new chat. Start talking.

On the phone and on the web, save one file at the end of a session: `my-record.md`.

## A folder, or Codex

If the chat can read the repository and create files, use the setup text, not a zip downloaded by hand. Codex is "works per the official docs, not run here". It reads `AGENTS.md`.

## Effort

The ordinary default is enough for all of this work. Do not raise effort only because this is visit prep. The optional stronger model, and how to switch to it, is a Claude step. It is named in `platform-facts.md`.

## Uploads

Crop or cover the ID number. A scanned letter uploaded as a PDF may arrive empty. Ask for a photo of the page. On the Free plan: 3 uploads a day (checked 11.11.2026).

The prep sheet is one complete file to save and print, unless the session really offers another document. Do not promise a format you cannot see.

## A new chat

New chat inside the project. Paste the handoff note first. "Catch up."

## Memory

Prefer project-only memory, so the medical project neither draws from nor feeds general memory. Where the switch sits was checked on 1.10.2026 and is pending a fresh check. Or turn memory off. Your screen wins.

## Account privacy

Turn off training on chats where the plan allows it. Exact clicks are pending on `privacy.html`.
