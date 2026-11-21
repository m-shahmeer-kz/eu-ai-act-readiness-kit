This is a readiness check, not legal advice.

**Result: HIGH-RISK AI system.** It analyses and filters job applications and evaluates candidates (pre-filter, pass/fail gate, scores, ranking, rejection e-mails), which is Annex III point 4(a) (Art 6(2)); it profiles candidates, so the Article 6(3) exemption cannot apply. It also has transparency duties under Article 50 (it generates e-mail text).

**Already applies:**
- AI literacy measures (Art 4) - since 2 Feb 2025
- Machine-readable marking of the generated e-mails (Art 50(2)) - since 2 Aug 2026 (2 Dec 2026 if already on the market before 2 Aug 2026)

**Coming next:**
- All high-risk provider duties (Art 9-17, 43 internal control, 47-49 declaration/CE/registration, 72-73) - from 2 Dec 2027 (376 days)
- Your employer customers (deployers) must then use it as instructed, assign human oversight, inform workers' representatives and candidates, and keep logs (Art 26).

**Do this first:**
1. Put a human decision in the loop: a recruiter must confirm every gate rejection and every e-mail before it goes out (Art 14). Fully automated rejections may also raise GDPR questions; get privacy advice.
2. Test for discrimination: location, language and work-authorisation criteria can act as proxies for nationality or origin; "soft skills" and "education" ratings need checking too (Art 10, Art 15).
3. Pin the models: the default `openrouter/auto` and env overrides can change the model without a code change, and the README reports 20+ point score differences across models.
4. Add persistent decision logs (Art 12): today there are only console output and e-mail files.
5. Continue the Annex IV draft (21 of 26 items have content, 9 still need the team) and start risk management and the quality management system.

**Files in `out/resume-job-matcher/`:** report.md, result.json, technical-documentation-draft.md, transparency-notices.md, ai-literacy-plan.md, scan.md, scan.json, profile.json

**Assumptions and open questions:** (no user was available)
- You are an EU start-up and the provider; employers and agencies deploy it; already offered in the EU, first release date unknown.
- Whether systems already on the market before 2 Dec 2027 get any transition (Art 111(2)) was not assessed by the kit.
- Company size unknown (SME relief may apply).

Please have a qualified EU AI Act lawyer confirm this before relying on it.
