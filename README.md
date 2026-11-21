# EU AI Act Readiness Kit

**Is your AI product high-risk under the EU AI Act?** An AI-agent skill (Claude Code, Codex, Cursor, Gemini CLI) that
checks an AI product against the EU AI Act: it scans the code for AI use, works out the risk category with the articles
behind it, lists every obligation with its date, and drafts the paperwork (Annex IV technical documentation, Article 6(3)
record, transparency notices, safeguards record, AI literacy plan). Built on the law as amended by the 2026 Digital
Omnibus (Regulation (EU) 2026/1744): high-risk rules from 2 Dec 2027 (Annex III) and 2 Aug 2028 (Annex I).

> **Not legal advice.** A readiness aid that can be wrong; every report asks you to have a qualified lawyer confirm it.

**[Get it on Agensi ($29) ↗](https://www.agensi.io/skills/eu-ai-act-readiness-kit-is-your-ai-product-high-risk)** · **[Results page ↗](https://m-shahmeer-kz.github.io/eu-ai-act-readiness-kit/)**

## Tested honestly

- **Blind test on the European Commission's own examples** (draft high-risk classification guidelines, May 2026, AI Act
  Service Desk): the skill was built on 4 areas, frozen, then a fresh AI agent classified **166 unseen examples** from
  5 other areas. **161 / 166 correct (97%)**: **64 / 64 high-risk systems recognised**, 5 / 102 not-high-risk systems
  wrongly flagged (all errors on the cautious side). Development areas: 144 / 146.
- **Buyer test on 6 real open-source AI products**: answers written down before the run; 5 match, 1 partly right
  (an image generator called "prohibited" where the law says "prohibited unless adequate safeguards"; fixed in v1.0.1).
- **44 automated tests** (CI on Python 3.10, 3.12, 3.13). Scan time on real repos: 0.1 to 3.9 s.

Details: [`results/`](results) and [`examples/`](examples). The skill source is sold on Agensi and is not in this repo.

## What it checks
- Is it an AI system, is it in scope, are you provider or deployer (Art 2, 3, 25)
- All 10 prohibited practices, incl. the new bans on non-consensual intimate imagery and CSAM from 2 Dec 2026 (Art 5)
- High-risk: Annex I products and the 25 Annex III use cases, the Article 6(3) exemption and the profiling rule
- Transparency (Art 50), general-purpose AI models (Art 53, 55), AI literacy (Art 4), SME / small mid-cap relief, penalties

## Limits
Readiness aid only; uses the Commission's draft guidelines, which may change; does not cover GDPR, copyright, product
liability or sector law; documentation drafts need the team's own risk decisions and test results.

Made by [Muhammad Shahmeer](https://m-shahmeer-kz.github.io/). © 2026, all rights reserved. Not affiliated with the European Commission.
