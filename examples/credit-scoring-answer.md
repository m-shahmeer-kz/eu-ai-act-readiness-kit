This is a readiness check, not legal advice.

**Result: HIGH-RISK AI system.** It is intended to establish the credit score / probability of default of individual borrowers so lenders can decide on loans, which is Annex III point 5(b) (Art 6(2)); because it profiles people's economic situation, the Article 6(3) exemption cannot apply. No transparency (Art 50) duties were found.

**Already applies:**
- AI literacy measures for your staff (Art 4) - since 2 Feb 2025
- Prohibited-practice check (Art 5) - since 2 Feb 2025: nothing flagged (credit scoring in the credit context is not social scoring)

**Coming next:**
- All high-risk provider duties: risk management (Art 9), data governance and bias examination (Art 10), technical documentation (Art 11, Annex IV), logs (Art 12), instructions for use (Art 13), human oversight (Art 14), accuracy/robustness/cybersecurity (Art 15), quality management (Art 17), conformity assessment by internal control (Art 43), declaration and CE marking (Art 47-48), EU database registration (Art 49), post-market monitoring and incident reporting (Art 72-73) - from 2 Dec 2027 (376 days)
- Your bank/lender customers (deployers) will need a fundamental rights impact assessment (Art 27) and the Art 26 deployer duties from the same date; they will ask you for the information to do it.

**Do this first:**
1. Decide about `age` and `number of dependants` as inputs and start a documented bias examination (Art 10); the notebook itself notes age drives the score.
2. Build a real validation: hold-out split, calibration, error rates per group. The only result today is one Kaggle figure (0.800498), labelled "accuracy" but to be checked against the competition metric.
3. Check the training data: Kaggle "Give Me Some Credit", origin and period undocumented, not known to be EU borrowers, licence for commercial use unclear. GDPR and EU consumer-credit rules may also apply; ask a lawyer.
4. Make the code reproducible (it uses scikit-learn modules that no longer exist; no pinned versions) and give it a version number.
5. Start the risk management file and quality management system; continue the Annex IV draft (12 of 26 items have content, 21 still need the team).

**Files in `out/Credit-scoring-model/`:** report.md, result.json, technical-documentation-draft.md, ai-literacy-plan.md, scan.md, scan.json, profile.json

**Assumptions and open questions:** (no user was available, so these are my assumptions)
- You are an EU start-up and the provider; customers (banks, lenders) deploy it; you do not use it yourselves.
- It is already offered in the EU in its current form; first release date unknown. Whether systems already on the market before 2 Dec 2027 get any transition (Art 111(2)) was not assessed by the kit; ask your lawyer.
- If it were only used to score companies (not natural persons) or only to detect fraud, it would fall outside 5(b).
- Company size unknown: if you are an SME or small mid-cap, lower fine caps and a simplified documentation form apply.

Please have a qualified EU AI Act lawyer confirm this before relying on it.
