# EU AI Act readiness report: Resume Job Matcher

> **Not legal advice. This is a readiness aid produced by software and an AI agent from the answers given. It can be wrong or incomplete, and the law and its guidance keep changing. Have a qualified lawyer confirm the classification and obligations before you rely on them.**

Prepared 2026-11-21 with EU AI Act Readiness Kit 1.0.0. Law version: Regulation (EU) 2024/1689 (AI Act) as amended by Regulation (EU) 2026/1744 (Digital Omnibus on AI, in force 27 July 2026). Rules checked on 21 Nov 2026.

## Result

**HIGH-RISK AI system**

Also: Limited risk: transparency duties (Article 50)

Your role(s): provider.

### Why

- Art 6(2) + Annex III 4(a): in scope, and it profiles people, so the Art 6(3) filter can never apply (Art 6(3) last subparagraph).

### Annex III use cases matched

- **4(a)**: Employment: recruitment or selection (targeted job ads, filtering applications, evaluating candidates)

Reasoning given: Step 1: README: 'screens a folder of resume PDFs against a job description and tells you who to interview'. Step 2: Annex III 4(a) covers analysing and filtering job applications and evaluating candidates; it pre-filters, gates (rejects), scores and ranks candidates. Step 3: it evaluates personal aspects (experience, skills, language, location), so it profiles natural persons and the Art 6(3) filter is unavailable. Step 5: a recruiter deciding afterwards does not change this.

Article 6(3) filter: not available: the system profiles natural persons.

## Obligations and deadlines

| When | Who | Article | Duty | What to do |
|---|---|---|---|---|
| applies now | provider and deployer | Art 4 | AI literacy | Take measures to support the AI literacy of staff and others who operate or use the system for you (training fitted to their role and the context). Since the 2026 amendment you must take measures, not guarantee a level. |
| applies now | provider (good practice) | Art 53(1)(b) (supplier's duty) | Get your GPAI supplier's documentation | Not a duty of yours, but useful evidence: ask your model supplier (Anthropic (claude-sonnet-4-5), OpenAI (gpt-5.6-luna, text-embedding-3-small), OpenRouter (openrouter/auto routing)) for its downstream documentation and keep it with your own records. |
| applies now | provider | Art 50(2) | Transparency | Mark AI-generated audio, image, video or text in a machine-readable, detectable way. |
| from 2027-12-02 (376 days) | provider | Art 9 | Risk management system | Run a documented, continuous risk process: identify foreseeable risks to health, safety and fundamental rights, estimate them, mitigate, test. |
| from 2027-12-02 (376 days) | provider | Art 10 | Data and data governance | Training, validation and test data must be relevant, representative, as error-free and complete as possible; examine and mitigate bias (special-category data may be processed for bias detection only under the strict safeguards of Art 10(5)). |
| from 2027-12-02 (376 days) | provider | Art 11 + Annex IV | Technical documentation | Write and keep up to date the Annex IV technical documentation before placing on the market. |
| from 2027-12-02 (376 days) | provider | Art 12, 19 | Record-keeping (logs) | Automatic event logs over the lifetime, enough to trace risks and monitor; keep at least 6 months. |
| from 2027-12-02 (376 days) | provider | Art 13 | Transparency and instructions for use | Give deployers clear instructions: purpose, accuracy, limits, risks, human oversight measures, input data, log handling. |
| from 2027-12-02 (376 days) | provider | Art 14 | Human oversight | Design for effective oversight by people: understand limits, avoid automation bias, override or stop the system. |
| from 2027-12-02 (376 days) | provider | Art 15 | Accuracy, robustness and cybersecurity | Declare accuracy metrics; resilience to errors and attacks (data poisoning, adversarial inputs, model flaws). |
| from 2027-12-02 (376 days) | provider | Art 17 | Quality management system | Written policies and procedures covering design, testing, data, risk, post-market monitoring, incidents, accountability (proportionate for SMEs/SMCs; simplified option Art 63). |
| from 2027-12-02 (376 days) | provider | Art 43 | Conformity assessment | Internal control (Annex VI) for most Annex III systems; notified body for some biometrics and for Annex I products. |
| from 2027-12-02 (376 days) | provider | Art 47, 48 | EU declaration of conformity and CE marking | Sign the declaration (Annex V) and affix CE marking. |
| from 2027-12-02 (376 days) | provider | Art 49 | Register in the EU database | Register yourself and the system before placing on the market (Annex VIII). |
| from 2027-12-02 (376 days) | provider | Art 72 | Post-market monitoring | Collect and analyse performance data after release, with a monitoring plan. |
| from 2027-12-02 (376 days) | provider | Art 73 | Serious incident reporting | Report serious incidents to the market surveillance authority (generally within 15 days). |
| from 2027-12-02 (376 days) | provider | Art 20 | Corrective actions | Fix, withdraw or recall non-conforming systems and inform others in the chain. |
| from 2027-12-02 (376 days) | provider | Art 16(l) | Accessibility | Meet EU accessibility requirements (Directives 2016/2102 and 2019/882). |

## Documents to prepare

- `ai-literacy-plan.md`
- `technical-documentation-draft.md`
- `transparency-notices.md`

## Penalties (Art 99)

- Prohibited practices: up to EUR 35 million or 7% of worldwide annual turnover.
- Most other obligations (incl. high-risk and transparency): up to EUR 15 million or 3%.
- Wrong or misleading information to authorities: up to EUR 7.5 million or 1%.
- SMEs, start-ups and small mid-caps: whichever of the two amounts is lower (Art 99(6), 99(6a)).

## Key dates

- **2024-08-01** AI Act enters into force. *(passed)*
- **2025-02-02** Prohibited practices (Art 5 a-h) banned; AI literacy duty (Art 4) applies. *(passed)*
- **2025-08-02** General-purpose AI model rules (Art 51-56), governance and penalties apply. *(passed)*
- **2026-07-27** Digital Omnibus on AI (Reg 2026/1744) in force: high-risk dates moved, Art 4 softened, SMC relief. *(passed)*
- **2026-08-02** Transparency duties (Art 50) apply: tell people they talk to AI, mark AI content, label deepfakes. *(passed)*
- **2026-12-02** New bans: AI that makes non-consensual intimate imagery or child sexual abuse material (Art 5(1)(ba),(bb)). Generative systems already on the market before 2 Aug 2026 must mark outputs (Art 111(4)).
- **2027-08-02** GPAI models placed on the market before 2 Aug 2025 must comply (Art 111(3)). National sandboxes due.
- **2027-12-02** High-risk rules apply to Annex III use cases (employment, education, credit, insurance, biometrics, ...).
- **2028-08-02** High-risk rules apply to AI in regulated products (Annex I: medical devices, toys, lifts, ...).
- **2030-08-02** High-risk systems used by public authorities that were already on the market must comply (Art 111(2)).

## Limits of this report

- It is only as good as the answers in the questionnaire. Re-run it when the product or its use changes.
- It applies the legal text and the Commission's draft guidelines (May 2026); final guidelines, harmonised standards and national rules may change the picture.
- It does not cover GDPR, product liability, copyright, consumer or sector law, which often apply too.

> Not legal advice. This is a readiness aid produced by software and an AI agent from the answers given. It can be wrong or incomplete, and the law and its guidance keep changing. Have a qualified lawyer confirm the classification and obligations before you rely on them.
