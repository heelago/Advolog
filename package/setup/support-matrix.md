# טבלת התמיכה, מה אומת ומה בתחום

<!-- Dated support matrix. Version 1.2.0. Fact rows live in platform-facts.md.
     This file does not name a model. -->

**נכון ל־11.11.2026 · גרסה 1.2.0.** Advolog הוא מסגרת הנחיות וקבצים שפועלת בתוך Claude ו־ChatGPT, לצד אתר מידע סטטי ולוח מקומי אופציונלי. האימות מתמקד במסע המשתמש, בשלמות הרשומות ובעמודי הבטיחות.

## מה אומת

| רכיב | היקף האימות | תאריך |
|---|---|---|
| **המסלול המלא ב־Claude וב־ChatGPT, גרסה 1.0** | ריצות חיות מקצה לקצה: התחלה, קליטה ושחזור, יצירת רשומות, המשך מהקבצים והפקת חומר לביקור | 2.8.2026 |
| **עמודי הבטיחות והמחקר, גרסה 1.0** | בלי אבחון, בלי המלצות טיפול ובלי מקורות מומצאים, לאורך תרחישים | 2.8.2026 |
| **טקסט הפתיחה בלי הורדה, גרסה 1.0** | ריאיון, קליטה והכנה מהירה מתוך הטקסט לבדו | 2.8.2026 |
| **הלוח המקומי** | חיבור תיקייה, הצגת הרשומות, אישור עדכונים, ייצוא גיבוי וכלי הפרטיות בדפדפן מחשב | 31.7.2026 |
| **גרסה 1.1.0** | נבדקה מול דפי העזרה ב־1.10.2026. לא הורצה חיה מקצה לקצה | 1.10.2026 |
| **גרסה 1.2.0** | נבנתה ונבדקה מקומית (`tools/build.py`, `tools/check.py`). **ריצה חיה בחשבונות אמיתיים: ממתינה.** רשימת התרחישים ב־`tests/README.md` | 11.11.2026 |

## עובדות פלטפורמה

<!-- facts:matrix -->
עובדות הפלטפורמה נבדקו מול דפי העזרה ב־11.11.2026 ונמצאות ב־`platform-facts.md`. שמות מודלים רק שם. המדריכים אומרים «ההגדרה המהירה» ו«הגדרת החשיבה העמוקה יותר». בדיקות שדורשות חשבון אמיתי (גודל שדה ההנחיות, איך נקראים קובצי פרויקט) ממתינות. אם המסך אצלך שונה, המסך קובע.
<!-- /facts:matrix -->

## גבולות התמיכה

- המסלול הנתמך בריצה חיה, כשתתבצע, הוא Claude באתר ובמחשב, ו־ChatGPT באתר. התאריך ייכתב בטבלה למעלה אחרי הריצה.
- Claude הוא המשטח הראשי. בודקים אם יש פרויקט Claude (שיחה ראשית אחת). אם המסך עדיין מראה פרויקט עם שדה הנחיות, גם זה נתמך. הנתיב לא הורץ בחשבון. ChatGPT נתמך כשיש חשבון שם, עם שדה ההנחיות של פרויקט.
- עוזרים אישיים שמותר להזכיר: Dot ו־Grok Bot. עוד לא הורצו כאן. Duet עדיין לא זמין בישראל, ואינו מסלול נתמך.
- שלוש דרגות: **אומת בריצה חיה** (Claude באתר ובמחשב, ChatGPT באתר, בתאריך שרשום בטבלה) · **עובד לפי התיעוד הרשמי, לא הורץ אצלנו** (Codex, Dot, Grok Bot) · **לא נבדק** (כל השאר, כולל Duet). מה שמופיע אצלכם הוא הקובע.
- האתר הוא דף נחיתה ותיעוד סטטיים. הוא אינו סביבת ההרצה.
- הלוח הוא נוחות בלבד. אם הדפדפן לא מציע גישה לתיקיות, ממשיכים דרך השיחה. בנייד משתמשים בשיחה, או בקובץ רשומה אחד (`my-record.md`).
- לא משתמשים בפרויקט משותף או בתיקייה משותפת לרשומות.

«אומת» אינו אומר «מובטח». הפלטפורמות משתנות. דיווחי תקלות מתקבלים בלי מידע רפואי ובלי פרטים אישיים.

## English

**As of 11.11.2026, version 1.2.0.** The 1.0 live runs stand. Version 1.2 was built and checked locally. A live run on real Claude and ChatGPT accounts is pending. The scripts are in `tests/README.md`.

Claude is the primary surface. ChatGPT is supported when that is the account you have.

Personal agents this project will name: Dot and Grok Bot. Not run here yet. Duet is not yet available in Israel, and is not a supported path.

Three tiers: **validated on a live run** (Claude on the web and on a computer, ChatGPT on the web, on the date in the table) · **works per the official docs, not run here** (Codex, Dot, Grok Bot) · **not tested** (everything else, including Duet). What you see on your screen is what counts.

Do not keep the record in a shared project or a shared folder.
