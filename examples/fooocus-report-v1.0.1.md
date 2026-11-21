# EU AI Act readiness report: Fooocus

> **Not legal advice. This is a readiness aid produced by software and an AI agent from the answers given. It can be wrong or incomplete, and the law and its guidance keep changing. Have a qualified lawyer confirm the classification and obligations before you rely on them.**

Prepared 2026-11-21 with EU AI Act Readiness Kit 1.0.1. Law version: Regulation (EU) 2024/1689 (AI Act) as amended by Regulation (EU) 2026/1744 (Digital Omnibus on AI, in force 27 July 2026). Rules checked on 21 Nov 2026.

## Result

**PROHIBITED from 2 Dec 2026 unless adequate safeguards are added (Art 5(1)(ba)/(bb) + 5(1a))**

Also: Limited risk: transparency duties (Article 50)

Your role(s): provider.

### Why

- Art 5(1)(ba)/(bb) + 5(1a): from 2 Dec 2026, placing on the market a system that can generate realistic intimate images of identifiable people or child sexual abuse material is prohibited unless it has reasonable and adequate safety measures to reliably prevent this (considering foreseeable misuse) and to correct reported misuse. The answers say these safeguards are missing.

### Note on prohibited practices (from the assessment)

BORDERLINE, flagged per the kit's rule ('borderline -> true'). Fooocus is a general image generator, not a 'nudifier', but: FaceSwap and inpainting take photos of real, identifiable people; the default checkpoint is photorealistic; the NSFW safety checker (extras/censor.py) exists but is OFF by default (modules/config.py default_black_out_nsfw=False) and users can load any Civitai checkpoint. So generating realistic intimate images of an identifiable person without consent, or CSAM, is a reasonably foreseeable misuse with no default safeguard. Whether Art 5(1)(ba)/(bb) reach a general-purpose generator with weak safeguards needs legal advice; turning the safety checker on by default, blocking FaceSwap/inpaint of real faces into sexual content and adding a CSAM classifier are the obvious mitigations before 2 Dec 2026.

## Obligations and deadlines

| When | Who | Article | Duty | What to do |
|---|---|---|---|---|
| applies now | provider and deployer | Art 4 | AI literacy | Take measures to support the AI literacy of staff and others who operate or use the system for you (training fitted to their role and the context). Since the 2026 amendment you must take measures, not guarantee a level. |
| applies now | provider (good practice) | Art 53(1)(b) (supplier's duty) | Get your GPAI supplier's documentation | Not a duty of yours, but useful evidence: ask your model supplier (Stability AI (SDXL base, via community fine-tunes such as JuggernautXL; GPAI status of SDXL unsure), OpenAI GPT-2 weights (local prompt expansion)) for its downstream documentation and keep it with your own records. |
| applies now | deployer | Art 50(4) | Transparency | Disclose that deepfake image, audio or video content is AI-generated or manipulated. |
| applies now | provider | Art 50(2) | Transparency | Mark AI-generated audio, image, video or text in a machine-readable, detectable way. |
| from 2026-12-02 (11 days) | provider | Art 5(1)(ba),(bb), 5(1a) | Safeguards against intimate deepfakes and CSAM | Keep reasonable and adequate technical safety measures that reliably prevent generating realistic intimate images of identifiable people without consent and child sexual abuse material, taking foreseeable misuse into account, and a way to correct reported misuse. Document them. Currently missing: without them, placing the system on the market is prohibited. |

## Documents to prepare

- `ai-literacy-plan.md`
- `safeguards-record.md`
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
- High-risk systems already on the market before the high-risk date may be covered only after a significant change in design (transitional rules, Art 111(2)); check the consolidated text with your lawyer.

> Not legal advice. This is a readiness aid produced by software and an AI agent from the answers given. It can be wrong or incomplete, and the law and its guidance keep changing. Have a qualified lawyer confirm the classification and obligations before you rely on them.
