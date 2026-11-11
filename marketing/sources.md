<!-- Second-reader check, 2026-11-11. Graphics are not built in this version.
     D33 and D34 measure the wait for the doctor the patient chose.
     Heela checked the Ministry of Health dashboard on 11.11.2026.
     The face label is: זמן המתנה לרופא לפי בחירת המטופל.
     Any graphic that uses D33 or D34 must print that on its face.
     tools/check.py fails a graphic that cites them without the label. -->

# Advolog marketing statistics: second-reader check

Checked 2026-11-11 (Asia/Jerusalem) by Grok Bot as the independent second reader (decision 46). Every High row in `MARKETING_DATA.md` (D1 to D32) was re-opened at its source today: PDFs and OECD StatLink workbooks were downloaded and searched, web pages were read in full. Nothing here is published or committed.

Status key:
- **yes**: value, year and geography match the source exactly.
- **corrected**: the number matches, but a label, page, year or source description in the marketing file was wrong or incomplete. The fix is in the note. Graphics should use the corrected label.
- **no**: the number does not match. (None found.)
- **not checked**: Medium or Low row, outside this pass, unless noted.

Local copies of every opened source are in `marketing/_src/` (box only, not for the repo).

## Summary

- High rows checked: 25 (D1, D2, D3, D5, D6, D7, D8, D9, D12, D13, D14, D15, D17, D18, D19, D20, D22, D23, D24, D26, D27, D28, D30, D31, D32).
- Verified as written: 18.
- Corrected (number right, label or reference fixed): 7 (D7, D12, D13, D19, D30, D31, D32).
- Failed (number wrong): 0.
- New rows added from today's gap search: D33 (MoH waiting-time program, national waits by specialty to April to June 2026) and D34 (Taub 2025, waits by district, April to June 2025). D20 gains a 1.2 million figure from the same High source, which closes decision 27.
- Decision 26 gap (a current, official consultation length): **not closed**. No official Israeli figure exists in anything opened today.

## High rows

| ID | Value (as confirmed) | Data year | Geography | Source URL | Strength | Checked | Verified | Note |
|---|---|---|---|---|---|---|---|---|
| D1 | Practising doctors per 1,000: Israel 3.5, OECD 3.9 | 2023 | Israel vs OECD | https://www.oecd.org/content/dam/oecd/en/publications/reports/2025/11/health-at-a-glance-2025_a894f72e/8f9e3f98-en.pdf (Table 1.6, p. 25) and https://www.oecd.org/en/publications/health-at-a-glance-2025_15a55280-en/israel_b3600fbc-en.html | High | 2026-11-11 | yes | Country note dated 13 Nov 2025. The OECD HTML pages return 403 to scripts but open in a normal reader; the PDF downloads directly. |
| D2 | Practising nurses per 1,000: Israel 5.6, OECD 9.2 | 2023 | Israel vs OECD | Same as D1 | High | 2026-11-11 | yes | Taub 2025 uses a different OECD average (9.5) and 5.57 for Israel. Use the OECD figures only, never mix. |
| D3 | Hospital beds per 1,000 (all beds, OECD definition): Israel 3.0, OECD 4.2 | 2023 | Israel vs OECD | Same as D1 | High | 2026-11-11 | yes | |
| D5 | Health spending: Israel USD 4,352 PPP per capita, 7.6% of GDP; OECD USD 5,967, 9.3% | 2024 (both columns of Table 1.6 are 2024) | Israel vs OECD | Same as D1 | High | 2026-11-11 | yes | The Taub 2025 full PDF (now opened) gives 7.3% of GDP for 2024 from CBS national accounts, and USD 3,941 PPP per capita. Different source and method. Keep OECD; never show both. |
| D6 | In-person doctor consultations per person: Israel 6.8 (2023), 8.1 (2019), 8.7 (2013); OECD31 average 6.5 (2023) | 2023, 2019, 2013 | Israel vs OECD31 | https://stat.link/rqt74h (Figure 5.16 workbook) | High | 2026-11-11 | yes | Report text: "Chile and Israel ... provide data for public providers only". |
| D7 | Teleconsultations per person: Israel 2.8, highest in 2023 | 2023 | Israel vs OECD | https://stat.link/dn3ys5 (Figure 5.17) and HaG 2025 PDF, Data and digital section | High | 2026-11-11 | corrected | Israel 2.8 and "Israel had the highest use in 2023" are verbatim. Correction: the "1.0 per patient per year" OECD figure is the trend average in Figure 9.15; the same-chart comparator in Figure 5.17 is the **OECD22 average of 0.9**. On a chart that shows Israel's 2.8 from Figure 5.17, use OECD22 0.9 as the comparator. |
| D8 | Total doctor consultations: Israel 9.6 (6.8 in person + 2.8 remote) | 2023 | Israel | https://stat.link/dn3ys5 | High | 2026-11-11 | yes | OECD22 averages in the same chart: 6.4 in person, 0.9 remote, 7.3 total. G7 currently pairs Israel's Figure 5.17 numbers with the OECD31 in-person 6.5 from Figure 5.16; use the OECD22 6.4 / 0.9 / 7.3 from the same chart instead. |
| D9 | Teleconsultations "over 25%" of doctor consultations in Denmark, Estonia, Israel, Portugal and Sweden; DERIVED 29% (2.8 / 9.6) | 2023 | Israel | HaG 2025 PDF, Access and coverage section | High (official wording) | 2026-11-11 | yes | Same paragraph: the OECD22 average share is 13%, a usable comparator. |
| D12 | Average wait for community specialist care: Clalit 22 days, Maccabi 29, Meuhedet 25, Leumit 23 | 2022 | Israel, four kupot | https://library.mevaker.gov.il/sites/DigitalLibrary/Documents/2024/2024.11-75A-PartB/2024.11-75A-PartB-601-Medical-Specialists.pdf | High | 2026-11-11 | corrected | Values exact. Page reference was wrong: it is printed page 17 (PDF page 18), not page 21. Each kupah measures differently ("ושיטות המדידה של כל אחת מהן"); say so in one line. |
| D13 | Longest: rheumatology 53 to 71 days, then endocrinology 47 to 53. Shortest: orthopedics 13 to 20, then ENT 15 to 21 | 2022 | Israel, four kupot | Same as D12 | High | 2026-11-11 | corrected | Values exact; same page fix as D12 (printed p. 17). |
| D14 | Appointments waiting over 90 days, top 50 specialties: Clalit about 31% (221,573 to 290,105); Maccabi about 43% (360,010 to 513,517); Leumit about 8% (109,665 to 118,308) | 2019 and 2022 | Israel, three kupot | Same as D12, printed pp. 20 to 21 | High | 2026-11-11 | yes | Caveat confirmed verbatim: some long appointments may be planned follow-ups that the kupot data cannot separate. |
| D15 | Clalit endocrinology, Tel Aviv district 69 days vs Jerusalem 42, North 37, Haifa 44 | 2022 | Israel, Clalit districts | Same as D12, printed p. 23 | High | 2026-11-11 | yes | |
| D17 | Doctors aged 55+: Israel 34.2% (2023), 40.3% (2013); OECD35 32.0% (2023) | 2023, 2013 | Israel vs OECD35 | https://stat.link/utqm17 (Figure 8.6) | High | 2026-11-11 | yes | Workbook values 34.246 and 40.287; OECD35 32.006. |
| D18 | General health literacy, Israel: 15% good/very good, 33% sufficient, 34% not quite sufficient, 18% inadequate; 52% in the bottom two. European sample: 15 / 40 / 33 / 13 | Fieldwork 15 Dec 2020 to 10 Jan 2021 | Israel, n = 1,315 | https://m-pohl.net/sites/m-pohl.net/files/2023-12/Health%20Literacy%20in%20Israel%20National%20Report%20HLS19%20-%20201902021.pdf | High | 2026-11-11 | yes | Chart 3 and body text match. The English summary says "approximately 50%"; the body gives 52%. Keep the COVID-period caveat. |
| D19 | Digital health literacy insufficient or low among 62.5% | Same as D18 | Israel | Same as D18 | High | 2026-11-11 | corrected | Number exact. Wording fix: the report says "insufficient or low" (English summary) and "לא מספקת או לא כל כך מספקת" (Hebrew body), not "inadequate and even low". |
| D20 | About 554,000 primary informal caregivers (349,000 / 63% caring for an older person; 205,000 / 37% for a person with a disability). 21% of adults care for someone with illness or disability. **Also: about 1.2 million people (21% of people aged 20+) cared unpaid for a family member with an illness or disability lasting six months or more** | 2019 | Israel | https://brookdale.jdc.org.il/wp-content/uploads/2023/09/Heb_Report_RR-943-23.pdf (sections 1.3 and 4.1) | High | 2026-11-11 | yes (plus a new figure) | The 1.2 million figure is in this High report, from the same CBS Social Survey 2019, and the report says it matches the CareGivers Israel estimate. 554,000 is the "primary caregiver" subset of the 1.2 million, so they may be shown nested (subset of), never added. This closes decision 27 without the Taub PDF. |
| D22 | 346,573 general disability pension recipients, December 2024, up 6.8% from Dec 2023; 6.4% of the eligible age range | Dec 2024 | Israel | https://www.btl.gov.il/Publications/Skira_shnatit/2024/Documents/chap-3-07-nehut-clalit.pdf | High | 2026-11-11 | yes | The BTL text has a typo ("כ-346,573 אלף"); the table value is 346,573. |
| D23 | 395,607 adults (up 6.2%) and 153,667 children (up 15.8%) receiving at least one disability-branch benefit | Dec 2024 | Israel | Same as D22 | High | 2026-11-11 | yes | |
| D24 | Average processing time of a general disability pension claim: 57.1 days; about 20% lower than 2008; fell in the latest year after a slight rise | 2024 | Israel | Same as D22 | High | 2026-11-11 | yes | Still no approval, rejection or appeal rates in this chapter. |
| D26 | 22% of US adults get health information from AI chatbots at least sometimes (7% often or extremely often, 15% sometimes); 85% from providers; 36% from social media | Survey 20 to 26 Oct 2025, published 7 Apr 2026 | United States, 5,111 adults | https://www.pewresearch.org/science/2026/04/07/users-of-social-media-and-ai-chatbots-for-health-information-are-more-likely-to-say-they-are-convenient-than-accurate/ and https://www.pewresearch.org/wp-content/uploads/sites/20/2026/04/PS_2026.4.7_health-information_REPORT.pdf | High, US only | 2026-11-11 | yes | |
| D27 | 32% used AI for health information or advice in the past year (29% physical, 16% mental); 41% of users (13% of all adults) uploaded personal medical information; 77% very or somewhat concerned about privacy | Survey 24 Feb to 2 Mar 2026, published 25 Mar 2026 | United States, 1,343 adults | https://www.kff.org/public-opinion/kff-tracking-poll-on-health-information-and-trust-use-of-ai-for-health-information-and-advice/ | High, US only | 2026-11-11 | yes | |
| D28 | 29% use AI tools or chatbots for health information at least monthly, up from 17% in June 2024; 71% never or only occasionally | Survey 7 to 31 May 2026, published 17 Jun 2026 | United States, 2,480 adults | https://www.kff.org/public-opinion/kff-tracking-poll-on-health-information-and-trust-use-of-social-media-and-ai-for-health-information-and-advice/ | High, US only | 2026-11-11 | yes | |
| D30 | "Up to 15% of diagnoses are estimated to represent a diagnostic error"; "Most people will experience at least one diagnostic error in their lifetime"; "80% of all harm caused by delayed or misdiagnosis may be preventable" | 2025 | International | https://www.oecd.org/content/dam/oecd/en/publications/reports/2025/03/the-economics-of-diagnostic-safety_6e0ed50b/fc61057a-en.pdf | High as a cited synthesis | 2026-11-11 | corrected | Quotes exact. Correction: this is **OECD Health Working Paper No. 176**, which states it does not represent the official views of the OECD. Label it "OECD Health Working Paper (2025)", not "OECD estimate". Decision 28 already keeps it out of the launch set. |
| D31 | 2.6 million US diagnostic errors a year, about 371,000 deaths and 424,000 permanent disabilities; direct cost estimated at 17.5% of health expenditure | As cited in 2025 | United States (cost share: "typical OECD country") | Same as D30 | High as a citation | 2026-11-11 | corrected | Same label fix as D30. The 17.5% is "this report estimates", i.e. the working paper's own estimate. |
| D32 | Ten-country average: 18% waited more than a week for a GP or nurse; 52% waited a month or longer for a specialist | 2023 (Commonwealth Fund 2023 International Health Policy Survey) | Ten surveyed countries, Israel not among them | https://www.oecd.org/en/publications/health-at-a-glance-2025_8f9e3f98-en/full-report/waiting-times_3a1021fa.html | High for those countries | 2026-11-11 | corrected | Values exact. Added the missing data year (2023 survey, Figure 5.13). Same paragraph adds "57% waited two days or longer" for primary care. |

## New rows from the gap search (decisions 26 and 27, 2024 to 2025 waits)

| ID | Value | Data year | Geography | Source URL | Strength | Checked | Verified | Note |
|---|---|---|---|---|---|---|---|---|
| D33 | MoH National Program for Measuring Waiting Times, community specialist care, national mean / median days. **April to June 2026:** neurology 55.9 / 59; psychiatry 51.8 / 54; child psychiatry 50.4 / 48; endocrinology 49.2 / 48; gastroenterology 46.4 / 46; dermatology 42.9 / 40; cardiology 33.3 / 29; urology 28.9 / 26; ophthalmology 24.3 / 17; gynecology 23.5 / 16; ENT 22.9 / 18; orthopedics 22.9 / 18. **April to June 2019** (where measured): dermatology 23.8 / 20; ENT 15.8 / 12; orthopedics 17.7 / 14; ophthalmology 16.6 / 10; gynecology 16.6 / 10. **October to December 2025:** neurology 60.0 / 65; endocrinology 53.4 / 57; psychiatry 52.6 / 59 | Quarterly, Q1 2019 to Q2 2026 | Israel, national, all four kupot | Dashboard: https://www.arcgis.com/apps/dashboards/e95ef054e35c42a7a7529831e1b7edfc ; data layer behind it: https://services5.arcgis.com/dlrDjz89gx9qyfev/arcgis/rest/services/waiting_time_country/FeatureServer/0 (owner `imohadmin`, last data edit 2026) | High candidate (official MoH data, current) | 2026-11-11 | new | Pulled from the public data layer the MoH dashboard itself reads, not a third party. Heela checked the dashboard on 11.11.2026: these figures are זמן המתנה לרופא לפי בחירת המטופל, the wait for the doctor the patient chose, not the wait for the first available doctor. Any graphic that uses D33 must say that on its face, in those words. Psychiatry and child psychiatry are measured only from October to December 2025 onward. This is the current replacement for the 2022 Comptroller data in G3; keep D12 to D14 for the kupah and 90-day story. |
| D34 | Wait for the doctor the patient chose, by district, median / mean days: South 20.0 / 18.5; Judea and Samaria 14.0 / 13.3; Tel Aviv 13.0 / 12.7; Center 10.0 / 11.5; Haifa 9.0 / 9.4; Jerusalem 6.0 / 8.7; North 6.0 / 5.7 | April to June 2025 | Israel, by district | Taub Center, Davidovitch, Lev and Gonen, "The Paradox of Israel's Healthcare System", State of the Nation 2025, Figure 9, p. 29: https://www.taubcenter.org.il/wp-content/uploads/2025/12/Health-2025-ENG-4.pdf (data: MoH National Program for Measuring Waiting Times) | High (full PDF opened, official data) | 2026-11-11 | new | Read off the chart labels; the figure image was checked. Heela checked the Ministry of Health dashboard on 11.11.2026: this series, like D33, is זמן המתנה לרופא לפי בחירת המטופל, the wait for the doctor the patient chose, not the wait for the first available doctor. Any graphic that uses D34 must say that on its face. Good for a regional disparity callout. |

## Medium and Low rows touched today

| ID | Status | Note |
|---|---|---|
| D4 | Now opened in the full Taub PDF | 1.76 vs 3.18 general beds confirmed in the executive summary (p. 5). Could be upgraded to High, but the definition caveat stays: never next to D3. |
| D10, D11 | not checked (Medium) | Still 2013 self-report. Not upgraded. See decision 26 below. |
| D16 | Opened in the full Taub PDF | "around 50 days" for neurology and endocrinology appears with no year or figure behind it. Superseded by D33, which shows the same order of magnitude with dates. Use D33. |
| D21 | Taub page re-read today | Text matches the file (1.2 million, hour bands 28 / 18 / 18 / 28%, "about 10% of the working-age population"). The PDF was not needed: the 1.2 million figure is now sourced to D20's High report. The hour bands remain Medium (Taub page only). |
| D25, D29 | not checked | Outside the launch set. |

## Gaps

**Decision 26: a current, official consultation length.** Not found. What exists:
- No Ministry of Health, kupah or OECD publication of measured visit length or official slot time was found. The MoH waiting-time program measures waits, not visit length.
- A Leumit study of 464,119 patients (Golan-Cohen et al., *Primary Health Care Research & Development*, 2025, https://doi.org/10.1017/s1463423625100364) used EMR-recorded visit durations for 2020 to 2021, but publishes only annual accumulated minutes per patient, not a per-visit mean.
- An observational IMAJ study (320 recorded encounters, 7 family doctors and 9 consultants) found a mean of 9.02 minutes: 10.39 with family doctors, 7.93 with consultants (https://www.ima.org.il/MedicineIMAJ/Article.aspx?aId=1395). Too small and undated for a graphic.
- Slot times of 10 to 15 minutes appear only in journalism.
- Result: default (a) stands. No minutes figure on any graphic; keep «לרופא יש חמש דקות» as rhetoric, never next to a measured number.

**Decision 27: caregivers.** Closed through D20 (see above).

**2024 to 2025 specialist waits.** Closed by D33 and D34.

**Still open, unchanged:** BTL approval and appeal rates; exceptions-committee data; the official 2025 ombudsman PDF (D25); the MoH burnout survey; a published-methods Israeli survey of AI use for health; Kessels recall; question-prompt-list effect sizes.
