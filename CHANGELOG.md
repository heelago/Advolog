# יומן שינויים · Changelog

כל גרסה: מה השתנה, במילים פשוטות. הרשומות שלך לא מושפעות משום עדכון — הסכימות רק מוסיפות, לעולם לא משכתבות.

Each release: what changed, in plain words. No update touches your records — schemas only add, never rewrite.

---

## 1.1.0 — 1.10.2026

### עברית

**חדש**

- **יחידת מסירה (היחידה השש־עשרה).** אחרי רישום, או אחרי שתיים־שלוש משימות, העוזרת מציעה לפתוח שיחה חדשה — בשורה אחת, עם הסיבה: שיחות ארוכות נעשות כבדות ופרטים מוקדמים נשמטים. שום דבר לא הולך לאיבוד, כי הרשומות בקבצים. היא כותבת פתק מסירה קצר שהשיחה הבאה קוראת ראשון: קובץ `handoff.md` בתיקיית הרשומות כשאפשר לכתוב אליה, ובלוק אחד להעתקה בכל מקום אחר. הצעה אחת לשיחה; סירוב מכובד בשקט.
- **מודל ומאמץ, שורה לכל סוג עבודה** — במדריכי ההתקנה, בפרומפט הפתיחה ובטבלת התמיכה. רישום יומיומי: Instant ב־ChatGPT, Medium ב־Claude. הכנה לביקור וסיכומים: Think או High ב־ChatGPT, High ב־Claude. יחידות המיומנות עצמן נשארות בלי שמות מודלים: הן רק אומרות, בשורה אחת, מתי כדאי יותר חשיבה.
- **קובץ להגיש לרופא/ה, ב־Claude.** דף ההכנה לביקור וטבלת התרופות נוצרים כ־Claude Doc (בתוכניות שכוללות אותו), שמייצאים ל־Word או ל־PDF. ה־Doc פרטי עד שמשתפים אותו, וקישור שיתוף נמצא במרחק לחיצה אחת. ב־ChatGPT הפלט נשאר כמו שהיה.
- **זיכרון ב־Claude** — סעיף חדש במדריך: הזיכרון פועל כברירת מחדל, נפרד לכל פרויקט, ובריאות לא נשמרת בו אלא אם מדליקים «Include sensitive topics in memory». ההמלצה: להשאיר כבוי, במיוחד למלווים. אינקוגניטו אינו זמין בתוך פרויקטים.
- **העלאת מסמכים.** לחתוך או לכסות את מספר תעודת הזהות לפני כל העלאה. ב־ChatGPT מכתב סרוק מעלים כתמונה ולא כ־PDF (תמונות בתוך PDF לא נקראות), ובתוכנית החינמית יש 3 העלאות ביום. Claude קורא PDF סרוק במלואו עד 100 עמודים.

**תוקן**

- **זיכרון ב־ChatGPT:** המדריך אמר שפרויקט שנוצר עם זיכרון רגיל אי־אפשר להעביר לזיכרון ברמת הפרויקט. זה כבר לא נכון — משנים בהגדרות הפרויקט, בלי ליצור פרויקט חדש. צילום המסך הישן הוסר עד שיצולם מחדש.

**שורה אחת כל אחד**

- לא הופכים את הלוח ל־ChatGPT Site: Site אפשר לפרסם לכל הרשת, ושיחות עליו עשויות לשמש לאימון.
- חיבורי נתוני הבריאות ב־Claude וב־ChatGPT זמינים רק בארצות הברית, ואינם רלוונטיים בישראל.
- איננו מבטיחים הכתבה בעברית.
- Custom GPTs יוצאים משימוש (11.12.2026). Advolog בנוי על Projects — בלי שינוי.

**איך זה נבדק.** כל עובדת פלטפורמה נבדקה מול דפי העזרה הרשמיים ב־1.10.2026 ומפורטת ב־`package/setup/support-matrix.md`. שתי טענות שלא עמדו בבדיקה לא נכנסו: ש־Claude לעולם אינו מסכם שיחות ארוכות (הוא כן, כשהרצת קוד מופעלת), ונתון על אורך שיחה בתוכניות החינמיות של ChatGPT (לא נמצא מקור רשמי). החדש בגרסה הזאת עוד לא הורץ בריצה חיה מקצה לקצה.

**בהמשך (לא בגרסה הזאת)**

- אריזה כ־Claude Skill (קובץ ZIP להתקנה).
- תזכורת שבועית מתוזמנת: «לרשום את השבוע».

### English

**New**

- **A handoff unit (the sixteenth).** After a log entry, or after two or three tasks, the assistant suggests starting a new chat — one line, with the reason: long chats get heavy and early details slip. Nothing is lost, because the records are in the files. It writes a short handoff note that the next chat reads first: a `handoff.md` file in the record folder where it can write there, one copy block everywhere else. One suggestion per chat; a decline is honored quietly.
- **Model and effort, one line per kind of work** — in the setup guides, the starter prompt, and the support matrix. Everyday logging: Instant on ChatGPT, Medium on Claude. Visit prep and summaries: Think or High on ChatGPT, High on Claude. The skill units themselves stay free of model names: they only say, in one line, when more thinking helps.
- **A file to hand the doctor, on Claude.** The visit prep sheet and the medications chart are produced as a Claude Doc (on plans that include it), which exports to Word or PDF. A Doc is private until shared, and a shared link is one tap away. On ChatGPT the output is unchanged.
- **Memory on Claude** — a new guide section: memory is on by default, separate per project, and leaves health out unless "Include sensitive topics in memory" is turned on. The recommendation: keep it off, caregivers especially. Incognito chats are not available inside projects.
- **Uploads.** Crop or cover the ID number before uploading anything. On ChatGPT a scanned letter goes up as a photo, not a PDF (images inside a PDF are not read), and the Free plan allows 3 uploads a day. Claude reads a scanned PDF in full up to 100 pages.

**Fixed**

- **ChatGPT memory:** the guide said a project created with regular memory could not be switched to project-only memory. That is no longer true — it is changed in the project's settings, with no need for a new project. The old screenshot was removed until it is retaken.

**One line each**

- Do not turn the dashboard into a ChatGPT Site: a Site can be published to anyone, and chats about it may be used for training.
- Health-data integrations in Claude and ChatGPT are US-only and do not apply in Israel.
- We do not promise Hebrew dictation.
- Custom GPTs are being retired (11.12.2026). Advolog is built on Projects — nothing changes.

**How this was checked.** Every platform fact was checked against the official help pages on 1.10.2026 and is listed in `package/setup/support-matrix.md`. Two claims that did not hold up were left out: that Claude never summarizes long chats (it does, when code execution is on), and a figure for chat length on ChatGPT's free plans (no official source found). What is new in this version has not yet had a full live end-to-end run.

**Next (not in this version)**

- Packaging as a Claude Skill (an installable ZIP).
- A weekly scheduled "log this week" nudge.

---

## 1.0.2 — 2.8.2026

שכבת המערכת הישראלית §7: כלי ראיות מקצועיים כגשר, לעולם לא כמקור לציטוט. · Israel layer §7: professional evidence tools as a bridge, never a citable tier.

## 1.0.1 — 2.8.2026

טבלת התמיכה מתעדת את הריצה החוזרת ב־ChatGPT; הערת פאנל הסנכרון בלוח. · The support matrix records the hardened ChatGPT rerun; dashboard sync-panel note.

## 1.0.0 — 2.8.2026

גרסה ראשונה. · First release.
