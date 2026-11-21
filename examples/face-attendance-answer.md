This is a readiness check, not legal advice.

**Result: HIGH-RISK AI system.** It identifies students by matching their faces from a live camera against an enrolled database (1:N), which I classified as remote biometric identification, Annex III point 1(a) (Art 6(2)); it is not 1:1 verification of a claimed identity, and the Article 6(3) exemption does not apply. No prohibited practice and no Art 50 duty were found.

**Already applies:**
- AI literacy measures (Art 4) - since 2 Feb 2025
- Prohibited-practice check (Art 5) - since 2 Feb 2025: nothing flagged (no face scraping, no emotion recognition, not law enforcement). Keep it that way: never add emotion or attention detection for students (Art 5(1)(f)).

**Coming next:**
- All high-risk provider duties (Art 9-17, 43, 47-49, 72-73) - from 2 Dec 2027 (376 days). For biometric systems a notified body is involved unless you apply harmonised standards (Art 43(1)).
- If schools that are public bodies use it, they have extra deployer duties (fundamental rights impact assessment, Art 27).

**Do this first:**
1. Decide how the product is meant to be used. A classroom camera that recognises seated students is "remote"; a kiosk where each student steps up, or a 1:1 check of a student who first presents an ID card, may fall outside 1(a). Narrowing the intended purpose this way is the legitimate route to a lower category, and must be reflected in the product, not just the wording.
2. Add a teacher confirmation step before attendance is saved or e-mailed (today it is written automatically above a fixed "confidence" of 67).
3. Measure accuracy, including per skin tone, age and gender; there are no tests or figures today.
4. Protect stored biometric data (face crops, model, CSVs are unencrypted; SMTP password meant to be typed into code). GDPR rules on biometric data and children may apply; get privacy advice.
5. Continue the Annex IV draft (17 of 26 items have content, 12 still need the team) and start risk management.

**Files in `out/Face-Recognition-Attendance-System/`:** report.md, result.json, technical-documentation-draft.md, ai-literacy-plan.md, scan.md, scan.json, profile.json

**Assumptions and open questions:** (no user was available)
- You are an EU start-up and the provider; schools/teachers deploy it; it is already offered in the EU, first release date unknown.
- "Remote" (without active involvement) is my conservative reading; how customers install the camera decides it.
- If you sell it for employee attendance too, Annex III 4(b) must also be checked.
- Company size unknown (SME relief may apply). Whether systems already on the market get a transition (Art 111(2)) was not assessed.

Please have a qualified EU AI Act lawyer confirm this before relying on it.
