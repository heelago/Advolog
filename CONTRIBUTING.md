# לתרום ל־Advolog

תודה שבאת. הפרויקט הזה נוגע באנשים ברגעים פגיעים, ולכן יש בו שכבה אחת שסגורה בכוונה: עמודי הבטיחות. כל השאר פתוח לשיפור.

## עמודי הבטיחות — לא פתוחים למשא ומתן

בקשת שינוי (PR) שמחלישה אחד מאלה תידחה, גם אם היא משפרת כל דבר אחר. אלו לא העדפות סגנון; זו הסיבה שאפשר לסמוך על הכלי:

1. שום אבחון. שם של מצב רפואי מופיע רק בתוך שאלה, רק עם מקור (המשתמש/ת העלו, או מקור מצוטט ומסווג), תמיד בניסוח «שווה לשאול האם X נשקל — בגלל (התבנית) + (המקור)», ותמיד עם כבוד לצוות: «נשקל והוחלט אחרת» היא תוצאה טובה.
2. שום ייעוץ טיפולי: לא להתחיל, להפסיק או לשנות תרופה, מינון, תזמון, מרווח או אוכל.
3. שום התחזות למערכות מקצועיות: פער נקרא בשמו, והגשר לאיש/אשת מקצוע אמיתיים מוצע.
4. שום ציטוט מומצא או משוער: מה שלא ניתן לאימות — מושמט, בקול. מספרים, ספים ומונחי קטגוריה — רק ממקורות שנשמרו בריצה הנוכחית, לעולם לא מהזיכרון של המודל.
5. רובדי הראיות לעולם לא מעורבבים, והתוויות קבועות: «מקורות רשמיים · פרסומים מדעיים · דיווחי מטופלים». בודקי תסמינים צרכניים הם קצה חוט, לא מקור.
6. מצוקה ומשבר: משאבים אמיתיים (101 · ער"ן 1201 · סה"ר), בלי שיטות, בלי בהלה; במצב קליטה — המשאב שזור בהכלה, לכל היותר פעם אחת בישיבה מעבר לשורת הכניסה. נימת «צוותים רפואיים רוצים לשמוע על זה מהר» שמורה לסימני הדחיפות בלבד.
7. הכלי לעולם לא שולח דבר: המשתמש/ת משדרים.
8. מזעור פרטים לעולם לא מתואר במונחי דה־זיהוי פורמליים.
9. המשתמש/ת מחליטים מה נקלט, נשמר ומשותף; סירוב מכובד בלי שכנוע חוזר.
10. אותיות דרגות היכולת (A/B/C) הן אוצר מילים פנימי ולעולם לא מופיעות בטקסט למשתמש.
11. שום עקיפה של חומות תשלום, התחברות או חסימה — מדלגים ואומרים.

## כללי עבודה על התוכן

- **המפה מנצחת.** בכל סתירה בין `package/core.md` ליחידת מיומנות, הליבה קובעת. שינוי התנהגות מתחיל בליבה.
- **סכימות מתפתחות בהוספה בלבד.** שום שינוי שדורש לשכתב רשומות קיימות של משתמשים.
- **מחרוזות עברית קבועות הן מילה־במילה.** תוויות הרובד, שורות המסגור ושלדי התבניות ב־`package/references/report-templates.md` אינם מנוסחים מחדש.
- **דוגמאות — מומצאות בלבד.** שום תוכן שמתאר אדם אמיתי, גם לא בעילום שם. אם זה קרה למישהו — זה לא נכנס כדוגמה.
- **עברית טבעית.** טקסט למשתמש נכתב עברית־קודם (לא תרגומית); הקול לפי `package/references/voice-canon.md`. שכבת הקבצים הפנימית — אנגלית.
- **בלי תלות בפלטפורמה בליבה.** התקנה פר־פלטפורמה חיה במדריכים בלבד.

## מה הכי שווה לתרום

- **עדכוני המערכת הישראלית** — `package/references/israel-system.md` הוא הקובץ שהכי צפוי להתיישן, ויש לו מחזור בדיקה מוצהר. עדכון = טענה + מקור רשמי (קופות, משרד הבריאות, כל־זכות, נוסח חוק) + תאריך. בלי מקור רשמי — לא נכנס.
- **מתכוני האוטומציה** במדריכים — השכבה הכי תלוית־פלטפורמה; כל מתכון חייב תאום ידני (פרומפט להדבקה) לצידו.
- תיקוני נגישות, RTL וניסוח באתר ובמדריכים.
- דיווחי באגים מפורטים (ראו תבניות ב־`.github/ISSUE_TEMPLATE/`).

## פרטיות בתרומות

בשום Issue, PR או דוגמה: אין שמות אמיתיים, אין תוכן רפואי אמיתי, אין צילומי מסך עם פרטים אישיים. תיאור התקלה מספיק תמיד.

## איך מגישים

Fork → ענף → שינוי ממוקד אחד → PR עם שלוש שורות: מה השתנה, למה, ואיך נבדק. שינויי פרומפטים מצרפים הליכת פרסונה קצרה (תרחיש מומצא) שמראה שההתנהגות מחזיקה. אם עוד אין לך GitHub — אפשר לשלוח הצעה בדוא"ל (הכתובת באתר) ונכניס אותה יחד.

---

# Contributing to Advolog

Thank you for being here. This project touches people at vulnerable moments, so one layer is deliberately closed: the safety walls. Everything else is open to improvement.

## The safety walls — not negotiable

A PR that weakens any of these will be declined, even if it improves everything else:

1. No diagnosis. A condition name appears only inside a question, only with provenance (user-raised, or a cited tier-labeled source), always framed "worth asking whether X has been considered — because (pattern) + (source)", always with deference: considered-and-set-aside is a good outcome.
2. No treatment advice: never starting, stopping, or changing a medication, dose, timing, spacing, or food.
3. No impersonating professional systems: gaps are named; the bridge to a real professional is offered.
4. No fabricated or approximated citations: the unverifiable is dropped, out loud. Numbers, thresholds, and category terms come only from sources retained in the current run, never from model memory.
5. Evidence tiers never blend, and the labels are fixed: "Official sources · Scientific publications · Patient reports". Consumer checkers are leads, never sources.
6. Distress and crisis: real resources (in Israel: 101 · ERAN 1201 · Sahar), no methods, no alarm; in capture mode the resource is woven into containment, at most once per sitting beyond the entry line. The "care teams want to hear about this quickly" tone is reserved for urgent-class signs only.
7. The tool never transmits anything: the user does.
8. Minimization is never described in formal de-identification terms.
9. The user decides what is captured, kept, and shared; a decline is honored without re-pitching.
10. Capability-tier letters (A/B/C) are internal vocabulary and never surface in user-facing text.
11. No circumventing paywalls, logins, or blocks — skip and say so.

## Working rules for the content

- **The map wins.** On any conflict between `package/core.md` and a skill, the core rules. Behavior changes start in the core.
- **Schemas evolve additively only.** Nothing may require rewriting users' existing records.
- **Fixed Hebrew strings are verbatim.** Tier labels, framing lines, and template skeletons in `package/references/report-templates.md` are never re-generated.
- **Examples are invented only.** Nothing that describes a real person, even anonymized.
- **Natural Hebrew.** User-facing text is Hebrew-first (never translated-sounding); voice per `package/references/voice-canon.md`. The internal file layer is English.
- **No platform dependence in the core.** Per-platform install lives in the guides only.

## What is most worth contributing

- **Israeli-system updates** — `package/references/israel-system.md` is the file most likely to age, and it has a declared review cadence. An update = claim + official source (kupot, Ministry of Health, Kol Zchut, statute text) + date. No official source — no entry.
- **Automation recipes** in the guides — the most platform-dependent layer; every recipe must ship with its manual twin (a paste-able prompt) beside it.
- Accessibility, RTL, and wording fixes on the site and guides.
- Detailed bug reports (see `.github/ISSUE_TEMPLATE/`).

## Privacy in contributions

In any issue, PR, or example: no real names, no real medical content, no screenshots carrying personal details. Describing the problem is always enough.

## How to submit

Fork → branch → one focused change → PR with three lines: what changed, why, how it was tested. Prompt changes attach a short persona walk (invented scenario) showing the behavior holds. No GitHub account — email the suggestion (address on the site) and we will land it together.
