# התקנה ב־Claude

Claude הוא המשטח הראשי. העוזרת עונה בשפה שכותבים בה. שמות המודלים רק ב־`platform-facts.md` ובפסקאות שהוא מרנדר. אם המסך שונה, המסך קובע.

לא שומרים את הרשומה בפרויקט משותף או בתיקייה משותפת. לא שולחים דבר. ההורדה רק אחרי כן.

## הדרך הראשית

לפני ההדבקה, בודקים ארבעה דברים בחשבון:

1. ביטול שימוש בשיחות לאימון, אם המתג קיים. הניסוח המדויק לא נקרא מחדש בדפדפן. המסך קובע.
2. פרטי בריאות מחוץ לזיכרון.
3. גישה לאינטרנט דלוקה, כדי שהעוזרת תוכל לקרוא את המאגר. אם היא כבויה, עוברים למסלול הגיבוי.
4. יצירת קבצים דלוקה, כדי שהיא תוכל להוריד ולהקים. אם היא כבויה, עוברים למסלול הגיבוי.

ואז מעתיקים את הבלוק העברי מ־`prompts/setup-from-repo.md` לשיחה חדשה. הבלוק האנגלי הוא הכפתור השני באתר. העוזרת קוראת את README, מסבירה מה Advolog ומה היא תעשה, ושואלת אם להוריד. רק כן ממשיך. אחר כך היא קוראת את `core.md` ופועלת לפיו.

## מסלול גיבוי, בלי אינטרנט או בלי יצירת קבצים

אומרים את זה במפורש. מדביקים את `core.md` בשדה ההנחיות (עד 7,000 תווים), ומעלים קובץ אחד: `web/advolog-modules.md`. בתוכנית החינמית של ChatGPT זו גם תקרת ההעלאות. אם הקובץ לא נקרא, `advolog-chatgpt-bundle.md`.

ה־zip נשאר למי שכבר מוריד תיקייה ביד. זו לא הדרך הראשית.

העלאת יכולת אחת, למי שכבר משתמש בזה: `advolog-skill.zip`. לפני כן מדליקים יצירת קבצים. `advolog-skills.zip` אינו נתיב ההעלאה.

איפה הרשומה באתר ובטלפון: `my-record.md`, שמירה אחת בסוף. שבעת הקבצים נשארים שווי ערך. לא ממירים בלי בקשה.

## מאמץ ומודל

<!-- facts:effort -->
לכל העבודה מספיקה ברירת המחדל, איפה שהתוכנית מציעה אותה. לא מעלים מאמץ רק כי זו הכנה לביקור. המודל החזק יותר מוצע פעם אחת, להחלטה קשה, למידע סותר, או לביורוקרטיה מסובכת, והעוזרת לא מחליפה אותו לבד. השם והבורר בפסקת המודל. אם המסך שונה, המסך קובע.
<!-- /facts:effort -->

<!-- facts:models-he -->
ברירת המחדל המומלצת, איפה שהתוכנית מציעה אותו: Opus 5.5 במאמץ בינוני. לא מכבים חשיבה. Fable הוא צעד רשות בתוכנית בתשלום, לא בחינם, ורק להחלטה קשה, למידע סותר, או לביורוקרטיה מסובכת. העוזרת מציעה את זה פעם אחת ולא מחליפה לבד. ב־Claude פותחים את בורר המודל ובוחרים Fable. נבדק מול דף הגישה לתוכניות ב־11.11.2026. המסך קובע.
<!-- /facts:models-he -->

## העלאות, וקובץ לרופא או לרופאה

לפני כל העלאה חותכים או מכסים את מספר תעודת הזהות. אם קובץ מגיע ריק או קטוע, אומרים זאת ומבקשים צילום של העמוד. לא מנחשים.

<!-- facts:uploads-claude -->
נבדק 11.11.2026: מסמך לייצוא קיים בכל התוכניות, כולל החינמית, ופתוח כברירת מחדל. בתוכנית החינמית אפשר לשתף בקישור, לא בהזמנה. המסמך פרטי עד שמשתפים אותו. לרופא או לרופאה פשוט יותר לייצא קובץ. לפני שיתוף, רשימת הבדיקה. אם המסמך לא מופיע בשיחה, הדף נמסר כקובץ מלא אחד.
<!-- /facts:uploads-claude -->

## שיחה חדשה

אחרי רישום, או אחרי שתיים־שלוש משימות, מוצעת שיחה חדשה, פעם אחת. שום דבר לא הולך לאיבוד, כי הרשומות בקבצים. באתר: New chat בתוך הפרויקט, ומדביקים את פתק המסירה כהודעה ראשונה. במחשב הפתק נשמר כ־`handoff.md`. מילת פתיחה: «תתעדכני».

## זיכרון

בריאות לא שייכת לזיכרון ארוך הטווח. הרשומה היא הקבצים.

<!-- facts:memory-claude -->
איפה המתג יושב, ומה שמו, ממתין לאימות בקובץ העובדות. ההמלצה עד אז: להשאיר פרטי בריאות מחוץ לזיכרון, במיוחד כשמתעדים עבור אדם אחר. מה שמופיע אצלכם הוא הקובע.
<!-- /facts:memory-claude -->

## פרטיות החשבון, שתי דקות

מבטלים שימוש בשיחות לאימון, איפה שהתוכנית מאפשרת. הצעדים המדויקים ממתינים לאימות ב־`platform-facts.md` ובדף `privacy.html` באתר. המסך קובע.

---

# Setup in Claude

Claude is the primary surface. The assistant answers in the language you write. Model names appear only in `platform-facts.md` and in the paragraphs it renders. If your screen differs, your screen wins.

Do not keep the record in a shared project or a shared folder. Nothing is sent. A download waits for a yes.

## The primary path

Before pasting, check four things:

1. Turn off training on chats if the switch exists. The exact wording was not re-read in a browser. Your screen wins.
2. Keep health details out of memory.
3. Web access on, so the assistant can read the repository. If it is off, use the fallback.
4. File creation on, so it can download and set up. If it is off, use the fallback.

Then paste the Hebrew block from `prompts/setup-from-repo.md` into a new chat. The English block is the second button on the site. The assistant reads the README, explains what Advolog is and what it will do, and asks whether to download. Only a yes continues. Then it reads `core.md` and follows it.

## Fallback, when there is no web access or no file creation

Say so plainly. Paste `core.md` into the instructions (at most 7,000 characters) and upload one file, `web/advolog-modules.md`. On ChatGPT Free that is also the upload cap. If that file is not read, use `advolog-chatgpt-bundle.md`.

The zip remains for someone who already downloads a folder by hand. It is not the primary path.

One skill upload, for people who already use that: `advolog-skill.zip`, with file creation on. `advolog-skills.zip` is not the upload path.

On the web and on a phone, the record is one file, `my-record.md`, one save at the end. The seven files stay equivalent. Do not convert unless asked.

## Effort and model

The recommended default is medium effort where the plan offers it. Do not raise effort only because this is visit prep.

<!-- facts:models-en -->
The recommended default, where the plan offers it: Opus 5.5 at medium effort. Do not turn thinking off. Fable is an optional step on a paid plan, not on Free, and only for a hard decision, conflicting information, or complex bureaucracy. The assistant offers it once and does not switch it itself. In Claude, open the model picker and choose Fable. Checked against the plan-access page on 11.11.2026. Your screen wins.
<!-- /facts:models-en -->

## Uploads, and a file for the doctor

Crop or cover the ID number before every upload. If a file arrives empty, say so and ask for a photo. Do not guess.

Checked 11.11.2026: an exportable document exists on every plan, including Free, and is on by default. On Free, sharing is by link, not by invitation. The document stays private until shared. For the doctor, export a file. The checklist comes first. If this session has no such document, the page is one complete file to save and print.

## A new chat

After a log, or after two or three tasks, a new chat is offered once. Nothing is lost. The records are in the files. On the web: New chat inside the project, and paste the handoff note first. On a computer the note is `handoff.md`. Opening word: "catch up".

## Memory

Health details do not belong in long-term memory. The files are the record. Where the switch sits is pending verification. Until then, keep health details out of memory, especially when the record is for someone else.

## Account privacy

Turn off training on chats where the plan allows it. The exact clicks are pending verification, on `privacy.html`. Your screen wins.
