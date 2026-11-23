# התקנה ב־Claude

Claude הוא המשטח הראשי. Advolog היא חבילה, לא אתר: שום דבר לא עובר דרכנו, ובכל דרך שפותחים אותה, העוזרת מכוונת אל ההקמה הכי מתאימה שיש. העוזרת עונה בשפה שכותבים בה. שמות המודלים רק ב־`platform-facts.md` ובפסקאות שהוא מרנדר. אם המסך שונה, המסך קובע.

הדרך הראשית ב־Claude, אם היא על המסך: פרויקט Claude. זו שיחה ראשית אחת. שיחה ארוכה אחת נעשית כבדה, ופרטים מוקדמים נשמטים. חוט צד יכול להיפתח לבד, למשל כדי להביא קבצים. זה רגיל. אין צורך לפתוח אותו או לנהל אותו. בודקים אם הפרויקט מופיע. אם לא, בודקים אם נשאר פרויקט עם שדה הנחיות. גם Duet, אם הוא על המסך, וגם Dot או Grok Bot, אם כבר נמצאים שם, הם אפשרויות שהעוזרת מציינת באותה הודעה. יש רק כן אחד, והוא מוריד את החבילה הציבורית. לא מניחים שמוצר קיים.

לא שומרים את הרשומה בפרויקט משותף או בתיקייה משותפת. לא שולחים דבר. ההורדה רק אחרי כן.

## הדרך הראשית

לפני ההדבקה, בודקים ארבעה דברים בחשבון:

1. ביטול שימוש בשיחות לאימון, אם המתג קיים. הניסוח המדויק לא נקרא מחדש בדפדפן. המסך קובע.
2. פרטי בריאות מחוץ לזיכרון.
3. גישה לאינטרנט דלוקה, כדי שהעוזרת תוכל לקרוא את המאגר. אם היא כבויה, עוברים למסלול הגיבוי.
4. יצירת קבצים דלוקה, כדי שהיא תוכל להוריד ולהקים. אם היא כבויה, עוברים למסלול הגיבוי.

ואז מעתיקים את הבלוק העברי מ־`prompts/setup-from-repo.md` לשיחה חדשה. הבלוק האנגלי הוא הכפתור השני באתר. העוזרת קוראת את README, מסבירה מה Advolog ומה היא תעשה, ובאותה הודעה אומרת מה על המסך ושואלת כן אחד. כן הזה מוריד רק את החבילה הציבורית. הוא אינו הסכמה לשום דבר אחר.

בדיאלוג של פרויקט חדש, נבדק 23.11.2026 בחשבון אחד: שם, «על מה רוצים לעבוד», והקשר. ויש מתג שדולק כברירת מחדל. הבדיקה רצה כשהוא דלוק. במילים פשוטות, זה המתג של השיחה הראשית שיכולה להתחיל עבודה בצד. המסך עצמו לא מסביר את המתג. מה קורה אם מכבים אותו לא נבדק. אם הניסוח אצלכם שונה, המסך קובע. השם על המסך, בשורה לבד:

`Project coordinator - Beta`

הצעד האחרון, לפני הריאיון, גם אחרי ההורדה וגם במסלול הגיבוי: שומרים את `web/instructions.md` (עד 7,000 תווים. הכפתור באתר נותן את הטקסט) במקום שההקמה שנבחרה שומרת אותו.

- פרויקט Claude, אם הוא על המסך. הנתיב נבדק 23.11.2026. גלגל השיניים ליד שם הפרויקט, אחר כך הגדרות הפרויקט, הלשונית שנקראת זיכרון, והשדה הנחיות הפרויקט. השדה הראה תקרה של 16,000 תווים, ו־7,000 תווים נשמרו. השמות על המסך, כל אחד בשורה:

`Project settings`

`Memory`

`Project instructions`

את `web/advolog-modules.md` ואת `my-record.md`, אם כבר יש, מוסיפים דרך הוספת הקשר. האפשרויות שנראו: העלאת קבצים, העלאת תיקייה, דרייב, תיקייה חדשה. השמות:

`Add context`

`Upload files`

`Upload folder`

`Drive`

`New folder`

נשארים בשיחה הראשית. בפרויקט עם שיחה אחת ממשיכים בה. פתק המסירה הוא למעבר למקום אחר, לא לשיחה חדשה בתוך אותו פרויקט. חוט צד להבאת הקבצים הוא רגיל. Claude יכולה לכתוב קבצי זיכרון משלה, למשל `MEMORY.md`, רק כהערת הקמה: שההקמה נעשתה ושהרשומה ב־`my-record.md`. לא מעתיקים לשם הסכמה, תוכן רפואי, או פרטים מזהים. היא לא משנה את הנחיות הפרויקט, ולא את `core.md`, בלי כן.

שם הקובץ הוא בדיוק `my-record.md`. אם ההעלאה קיבלה קידומת, משנים את השם. הורדה, נבדק 23.11.2026 בחשבון אחד: התפריט היה מוסתר. בודקים את המסך. הסרה מההקשר הייתה בלחיצה ימנית. בודקים את המסך. אם אומרים שהרשומה הוסרה, או שהקובץ לא בהקשר עכשיו, מה שנשאר בהיסטוריה אינו הרשומה.
- פרויקט עם שדה הנחיות, אם הוא עדיין על המסך: מדביקים בשדה, מעלים את הקובץ, מצרפים את `my-record.md`, ורק אז שיחה חדשה בתוך הפרויקט.
- תיקייה במחשב: סוגרים ופותחים מחדש את `package/` כדי ש־`CLAUDE.md` ייטען.

בלי הצעד הזה ההנחיות לא נשארות. אם המסך שונה, המסך קובע.

## מסלול גיבוי, בלי אינטרנט או בלי יצירת קבצים

אומרים את זה במפורש, ועושים את אותו צעד אחרון בלי ההורדה מהמאגר. מדביקים את `web/instructions.md` ומעלים קובץ אחד: `web/advolog-modules.md`. אם הקובץ לא נקרא, `advolog-chatgpt-bundle.md`.

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

## המשך, ופתק למעבר

אחרי רישום, או אחרי שתיים־שלוש משימות, אפשר פתק מסירה, פעם אחת. בפרויקט Claude עם שיחה ראשית אחת נשארים באותה שיחה. הפתק הוא למעבר: פרויקט חדש, עוזר אחר, או שיחה בלי הקובץ. לא אומרים «שיחה חדשה» בתוך הפרויקט הזה. שיחה חדשה נשארת לחשבון שעדיין יש בו שדה הנחיות, ול־ChatGPT. שום דבר לא הולך לאיבוד רק אם ההמשך באמת פותח את אותו `my-record.md` (או את שבעת הקבצים), ושההנחיות הקבועות כבר שמורות. אם הקובץ נשאר רק בארגז כלים זמני, מורידים עותק לפני המעבר. פתק לבדו אינו מספיק. מה שנשאר רק בהיסטוריית השיחה אינו הרשומה. במחשב הפתק נשמר כ־`handoff.md` ליד הקבצים. מילת פתיחה במקום החדש: «תתעדכני». לפני טיוטה עבור אדם אחר, בודקים שהקובץ מצורף עכשיו ושהפרופיל נקרא ממנו. אם אין הסכמה, או שהיא לא נקראת, לא כותבים את הטיוטה, ואומרים למה. הרישום הפרטי נשאר. אחרי טיוטה, עוצרים. לא מוסיפים שאלה.

## זיכרון

בריאות לא שייכת לזיכרון ארוך הטווח. הרשומה היא הקבצים.

<!-- facts:memory-claude -->
איפה המתג יושב, ומה שמו, ממתין לאימות בקובץ העובדות. ההמלצה עד אז: להשאיר פרטי בריאות מחוץ לזיכרון, במיוחד כשמתעדים עבור אדם אחר. מה שמופיע אצלכם הוא הקובע.
<!-- /facts:memory-claude -->

## פרטיות החשבון, שתי דקות

מבטלים שימוש בשיחות לאימון, איפה שהתוכנית מאפשרת. הצעדים המדויקים ממתינים לאימות ב־`platform-facts.md` ובדף `privacy.html` באתר. המסך קובע.

---

# Setup in Claude

Claude is the primary surface. Advolog is a package, not a site: nothing passes through us, and whichever way you open it, your assistant guides you to the best available setup. The assistant answers in the language you write. Model names appear only in `platform-facts.md` and in the paragraphs it renders. If your screen differs, your screen wins.

The primary Claude route, when it is on the screen: a Claude Project. That is one main conversation. One long session gets heavy, and early details slip. A side thread may start on its own, for example to fetch files. That is normal. You do not need to open it or manage it. Check whether the Project is there. If it is not, check whether an older project with an Instructions field is still there. Duet, if it is on the screen, and Dot or Grok Bot, if you are already there, are options the assistant names in the same message. There is only one yes, and it downloads the public package. Do not assume a product is present.

Do not keep the record in a shared project or a shared folder. Nothing is sent. A download waits for a yes.

## The primary path

Before pasting, check four things:

1. Turn off training on chats if the switch exists. The exact wording was not re-read in a browser. Your screen wins.
2. Keep health details out of memory.
3. Web access on, so the assistant can read the repository. If it is off, use the fallback.
4. File creation on, so it can download and set up. If it is off, use the fallback.

Then paste the Hebrew block from `prompts/setup-from-repo.md` into a new chat. The English block is the second button on the site. The assistant reads the README, explains what Advolog is and what it will do, and in the same message says what is on the screen and asks for one yes. That yes downloads the public package only. It is not consent for anything else.

On the new-project dialog, checked 23.11.2026 on one account: a name, what you want to work on, and context. A switch is on by default. The test ran with it on. In plain words, that is the switch for the main conversation that can start side work. The screen itself does not explain the switch. What happens if you turn it off was not tested. If the wording differs, the screen wins. The label is `Project coordinator - Beta`.

The last step, before onboarding, on the web route and on the fallback: save `web/instructions.md` (at most 7,000 characters; the site button gives that text) where the chosen setup keeps it.

- A Claude Project, if it is on the screen. The path was checked 23.11.2026. The gear next to the project name, then Project settings, the tab called Memory, and the Project instructions field. The field showed a 16,000 character limit, and 7,000 characters were saved. Add `web/advolog-modules.md` and `my-record.md`, if it already exists, with Add context. The choices seen were Upload files, Upload folder, Drive, and New folder. Stay in the main conversation. On a project with one chat, continue there. The handoff note is for a move to another place, not a new chat inside this project. A side thread that fetches the files is normal. Claude may write its own memory files, such as `MEMORY.md`, only as a setup note: setup is done and the record lives in `my-record.md`. Do not copy consent, medical details, or identifiers into them. It does not change Project instructions, or `core.md`, without a yes.

The record file is named exactly `my-record.md`. If an upload arrives with a prefix, rename it. Downloading, checked 23.11.2026 on one account: the control was in a hidden menu. Check the screen. Removing a file from Context was a right-click. Check the screen. If they say the record was removed, or the file is not in Context now, what remains in the chat history is not the record.
- A project with an Instructions field, if it is still on the screen: paste into the field, upload the file, attach `my-record.md`, and only then open a new chat inside the project.
- A folder on a computer: close and reopen `package/` so `CLAUDE.md` or `AGENTS.md` is in scope.

Without that step the instructions do not stay. If the screen differs, the screen wins.

## Fallback, when there is no web access or no file creation

Say so plainly, and do that same last step without fetching the repository. Paste `web/instructions.md` and upload one file, `web/advolog-modules.md`. On ChatGPT Free that is also the upload cap. If that file is not read, use `advolog-chatgpt-bundle.md`.

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

## Continuing, and a note for a move

After a log, or after two or three tasks, a handoff note may be offered once. On a Claude Project with one main chat, stay in that chat. The note is for a move: a new project, another assistant, or a chat without the file. Do not say "new chat" inside this project. A new chat remains for an account that still has an Instructions field, and for ChatGPT. Nothing is lost only if the continuation actually opens the same `my-record.md` (or the seven files), and the standing instructions are already saved. If the file is only in a temporary sandbox, download a copy before you move. The note alone is not enough. What remains only in the chat history is not the record. On a computer the note is `handoff.md` beside the files. Opening word in the new place: "catch up". Before a draft for someone else, check that the file is attached now and that the profile is read from it. If consent is missing, unreadable, or declined, do not write the draft, and say why. Private logging stays. After a draft, stop. Do not add a question.

## Memory

Health details do not belong in long-term memory. The files are the record. Where the switch sits is pending verification. Until then, keep health details out of memory, especially when the record is for someone else.

## Account privacy

Turn off training on chats where the plan allows it. The exact clicks are pending verification, on `privacy.html`. Your screen wins.
