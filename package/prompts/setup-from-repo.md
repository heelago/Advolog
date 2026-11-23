# Setup from the repository (paste into a new chat)

<!-- Hebrew is the default paste. English is the other copy button.
     Each block stays under 10,000 characters. No model names.
     {{ADVOLOG_RELEASE_REF}} is replaced at build time with the release tag.
     The tag is created only at release. A yes fetches the public package only.
     The assistant does not download until the user says yes, and does not send anything.
     The last step puts package/web/instructions.md into the private project
     (or reopens package/ for a folder install) before onboarding. -->

## עברית

```
את מקימה את Advolog רק אחרי שאאשר. אל תשלחי, תפרסמי או תעבירי שום דבר לאף אחד. אל תורידי קבצים לפני שאענה כן. כן כאן הוא רק להורדת החבילה הציבורית, לא הסכמה לשום דבר אחר.

אם אין לך גישה לאינטרנט, או שאין לך אפשרות ליצור קבצים, עצרי בשורה אחת ואמרי את זה. אז לא מורידים. עוברים ישר לצעד 5.

אם יש גישה:
1. פתחי את https://github.com/heelago/Advolog/blob/{{ADVOLOG_RELEASE_REF}}/README.md ואת https://raw.githubusercontent.com/heelago/Advolog/{{ADVOLOG_RELEASE_REF}}/README.md. קראי את README. אם הדף לא נפתח, אמרי את זה. אל תמציאי מה כתוב בו.
2. הסבירי לי בעברית פשוטה מה Advolog, מה היא תעשה, ומה היא לא תעשה: לא מאבחנת, לא ממליצה על טיפול, לא שירות חירום, ולא שולחת דבר בשבילי.
3. שאלי אם להוריד את החבילה הציבורית בלבד. רק תשובה של כן ממשיכה.
4. אחרי כן הורידי את package/ מ־https://github.com/heelago/Advolog/tree/{{ADVOLOG_RELEASE_REF}}/package כולל https://github.com/heelago/Advolog/blob/{{ADVOLOG_RELEASE_REF}}/package/core.md ואת https://raw.githubusercontent.com/heelago/Advolog/{{ADVOLOG_RELEASE_REF}}/package/core.md. אל תשני את core.md. אמרי איפה הקבצים באמת נחתו: תיקייה מקומית אמיתית, קובץ שאפשר להוריד, או רק ארגז כלים זמני. אם זו לא תיקייה מקומית, תני לי עותק להורדה.
5. לפני כל שיחת המשך, באתר: פרויקט פרטי. הדביקי בשדה ההנחיות את package/web/instructions.md, והציעי לי את הטקסט המדויק. העלי את package/web/advolog-modules.md. צרפי את my-record.md אם כבר יש. רק אז פתחי שיחה חדשה בתוך הפרויקט. במחשב, בתיקייה: סגרי ופתחי מחדש את package/ כדי ש־CLAUDE.md או AGENTS.md ייטענו. בלי הצעד הזה ההנחיות לא נשארות לשיחה הבאה.
```

## English

```
Set up Advolog only after I agree. Do not send, post, or forward anything to anyone. Do not download any files before I say yes. Yes here only fetches the public package. It is not consent for anything else.

If you cannot open the web, or you cannot create files, stop in one line and say so. Then do not download. Go straight to step 5.

If you can:
1. Open https://github.com/heelago/Advolog/blob/{{ADVOLOG_RELEASE_REF}}/README.md and https://raw.githubusercontent.com/heelago/Advolog/{{ADVOLOG_RELEASE_REF}}/README.md. Read the README. If the page does not open, say so. Do not invent what it says.
2. Explain in plain language what Advolog is, what it will do, and what it will not do: it does not diagnose, recommend treatment, handle emergencies, or send anything for me.
3. Ask whether to download the public package only. Only a yes continues.
4. After that, download package/ from https://github.com/heelago/Advolog/tree/{{ADVOLOG_RELEASE_REF}}/package including https://github.com/heelago/Advolog/blob/{{ADVOLOG_RELEASE_REF}}/package/core.md and https://raw.githubusercontent.com/heelago/Advolog/{{ADVOLOG_RELEASE_REF}}/package/core.md. Do not change core.md. Say where the files actually landed: a real local folder, a downloadable file, or only a temporary tool sandbox. If it is not a local folder, give me a downloadable copy.
5. Before any later chat, on the web: a private project. Paste package/web/instructions.md into the project Instructions, and offer me that exact text. Upload package/web/advolog-modules.md. Attach my-record.md if it already exists. Only then open a new chat inside the project. On a computer, in a folder: close and reopen package/ so CLAUDE.md or AGENTS.md is loaded. Without this step the instructions do not stay for the next chat.
```
