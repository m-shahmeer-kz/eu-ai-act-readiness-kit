# Technical documentation (Annex IV draft): Resume Job Matcher

> **Not legal advice. This is a readiness aid produced by software and an AI agent from the answers given. It can be wrong or incomplete, and the law and its guidance keep changing. Have a qualified lawyer confirm the classification and obligations before you rely on them.**

> Draft generated 2026-11-21 by `aiact.py assess`, then completed by the AI agent from the repository (readme.md,
> LOOP.md, docs/*.md, matcher/*.ts, evals/*.ts, package.json, .env-example). Test and eval results quoted below are the
> authors' own records in LOOP.md; they were not re-run for this draft. Every **[TO FILL]** needs an answer from the team.
> Keep this document for 10 years after placing on the market (Art 18).

## 1. General description of the AI system

**(a) Intended purpose, provider name, system version and its relation to previous versions**

- Intended purpose: employers and recruiters screen a folder of candidate resume PDFs against a job description; the
  system "tells you who to interview" (readme.md), rejects candidates who fail hard constraints, scores and ranks the
  rest, and drafts invite/rejection e-mails.
- Provider: [TO FILL] legal name and address (not named in the repository).
- Version: 2.0.0 (`package.json`). The TypeScript CLI (`matcher/`) replaced a legacy Python implementation
  (`resume_matcher.py`), still shipped for OCR and PDF regeneration, which uses a different scoring model whose numbers
  are "not comparable" (readme.md).

**(b) How it interacts with hardware or software (incl. other AI systems) not part of it**

- Calls third-party GPAI models through the Vercel AI SDK (`ai`, `@ai-sdk/anthropic`, `@ai-sdk/openai`,
  `@openrouter/ai-sdk-provider`): default models in `matcher/config.ts` are `claude-sonnet-4-5` (Anthropic),
  `gpt-5.6-luna` (OpenAI) and `openrouter/auto` (OpenRouter, which chooses the underlying model per request; default
  mode). Embeddings: `text-embedding-3-small` (OpenAI / via OpenRouter).
- Reads resume PDFs with `unpdf` (embedded text only; scanned PDFs fail). Resume text is sent to the chosen provider.

**(c) Versions of relevant software or firmware and version-update requirements**

- Node 20+ (tested on 22). Dependencies with caret ranges in `package.json` (e.g. `ai ^7.0.0`, `zod ^3.25.76`,
  `unpdf ^1.8.1`); legacy Python dependencies in `requirements.txt`. Model ids can be overridden by environment variables
  (`ANTHROPIC_MODEL`, `OPENAI_MODEL`, `OPENROUTER_MODEL`), so the model actually used can change without a code change.
- [TO FILL] pinned versions for releases and the policy for model changes.

**(d) All forms in which it is placed on the market (packages, APIs, downloads)**

- Repository form: command-line tool run with `npm run match -- <job file> <resume folder> --api <mode>`.
  [TO FILL] the start-up's product form (CLI, hosted service, API).

**(e) Hardware it is intended to run on**

- Any machine that runs Node 20+; inference runs at the model provider. [TO FILL]

**(f) Photos/illustrations of external features and internal layout (if part of a product)**

- Not applicable (software only).

**(g) Basic description of the user interface provided to the deployer**

- CLI. Console output: gate questions with severity, then candidates sorted by score with label and red-flag emojis,
  gated-out candidates listed with the disqualifying question and quoted evidence, errors listed separately, and a token
  and cost line. Files in `out/<job-slug>/`: `<name>_response.txt` (e-mail), optional `<name>_unified.md`,
  `job_description_enhanced.txt`.

**(h) Instructions for use for the deployer (and basic UI description)**

- readme.md gives usage, options and a "Known limitations" section (compensatory scores, cross-model variance of 20+
  points, topical-only pre-filter, no OCR) and a data-handling note. It does not yet cover all Art 13 items (intended
  purpose limits, accuracy per group, human oversight measures, log handling). [TO FILL]

## 2. Detailed description of the elements and of the development process

**(a) Methods and steps of development, incl. pre-trained systems or third-party tools used**

- No model is trained by the provider; behaviour is defined by prompts and structured-output schemas (zod) sent to the
  third-party models in 1(b). Development is tracked in LOOP.md and design docs in `docs/` (C1 gate, C2 anchors).
  Pipeline per run: (1) extract job requirements and weights (LLM, once); (2) derive 2-5 gate questions with severity
  1-10 (LLM, once); (3) extract PDF text; (4) optional embedding pre-filter keeps the top n by cosine similarity;
  (5) gate: LLM answers PASS/FAIL/UNCERTAIN with a quoted resume span; (6) survivors: LLM rates 7 criteria;
  (7) optional e-mail per candidate; (8) optional pool summary.

**(b) Design specifications: general logic, algorithms, key design choices and rationale, assumptions, intended users, optimisation targets, trade-offs**

- Gate rule (`matcher/gate.ts`, pure code): a FAIL on a question with severity >= 7 (`BLOCKING_SEVERITY`) rejects the
  candidate and skips scoring; UNCERTAIN or missing answers pass, a design choice "deliberately set for recall".
  Gate questions are restricted by prompt to work location or authorisation, on-site presence, legally required
  licences and explicit "must" items.
- Scoring: 7 criteria (language proficiency, education level, years of experience, technical skills, certifications,
  soft skills, location) rated 0-4 on an anchored scale (100/75/50/25/0), evidence quoted before the level; final score =
  weighted mean with weights extracted per job by the LLM. Level 0 raises a red flag sized by weight.
- E-mails: invite if score >= threshold (default 90), otherwise reject; gated-out candidates always get a rejection.
- Pre-filtered candidates are listed as skipped and get no e-mail.
- Trade-offs documented by the authors: scores are compensatory; location/work authorisation is both gated and scored
  ("double counting", LOOP.md); the pre-filter can drop strong candidates with different vocabulary.

**(c) System architecture: how components build on each other; compute used to develop, train, test and validate**

- `config.ts` (options, models) -> `pdf.ts` (text) -> `prefilter.ts` (embeddings, cache `out/.embedding-cache.json`
  keyed on resume content) -> `gate.ts` -> `match.ts` (scoring, e-mails, summaries) -> `scoring.ts` (pure aggregation) ->
  `bands.ts` (labels) -> `index.ts` (orchestration, concurrency 4 by default). `usage.ts` wraps calls to count tokens and
  cost. Compute: provider-side inference; [TO FILL] development compute if relevant.

**(d) Data requirements: datasheets on training methods and data sets (provenance, scope, characteristics, collection, labelling, cleaning)**

- No training data (no model training). Inputs at run time: the deployer's job description and candidates' resumes.
  Evaluation data: 5 synthetic fixtures in `evals/fixtures.ts` (e.g. `strong-frontend-match`,
  `backend-vs-frontend-mismatch`, `location-hard-miss`, `prompt-injection-resistance`, `email-uses-real-name`).
- [TO FILL] information from the GPAI providers about their training data (Art 53(1)(b) downstream documentation), and
  a representative, labelled evaluation set (LOOP.md item C8: "blocked until 10-20 labeled past screens exist").

**(e) Human oversight measures (Art 14) and technical measures to help deployers interpret outputs**

- Present: every gate rejection is shown with the question and the quoted resume span; criterion ratings carry quoted
  evidence; gated-out and pre-filtered candidates are listed, "so nothing disappears quietly"; e-mails are written to
  files, not sent. Missing: no step that requires a human to confirm a rejection or an e-mail; no way to override a gate
  decision inside the tool. [TO FILL]

**(f) Pre-determined changes to the system and its performance, with technical solutions for continuous compliance**

- Planned changes are listed in LOOP.md backlog (C2b calibration fixture, C2c per-criterion anchors, C3 human-set
  weights, C4 fewer score bands, C5-C9). [TO FILL] which of these are pre-determined changes and how compliance is
  kept when they ship or when the provider's model changes.

**(g) Validation and testing procedures, metrics (accuracy, robustness, discriminatory impact), test logs and signed test reports**

- Unit tests: 55 `test(` cases in 5 files (`bands`, `gate`, `scoring`, `config`, `prefilter`); `npm test`.
- Evals: `npm run eval`, 5 fixture assertions (match band, red-flag firing, prompt-injection resistance, website
  extraction, e-mail personalisation), live model, defined in LOOP.md as "definition of green".
- Recorded results (LOOP.md, authors' records, not verified here): 5/5 evals on gpt-5.6-luna and gpt-5-mini
  (2026-08-27/28); same fixture scored 24 (gpt-5.6-luna) vs 55 (gpt-5-mini); after C2, cross-model spread on the target
  fixture 31 -> 23 but mean spread across four fixtures 11.0 -> 16.0; prompt-injection fixture spread 3 -> 27.
- No accuracy against real hiring outcomes and no discriminatory-impact testing exist. No signed test reports. [TO FILL]

**(h) Cybersecurity measures**

- Prompts tell the model to treat the resume "as data, not instructions"; an eval fixture tests prompt-injection
  resistance; LLM outputs are constrained to zod schemas; website values that look invalid are discarded. API keys come
  from `.env`. Not present: access control, encryption of `out/` and the embedding cache (which hold personal data).
  [TO FILL]

## 3. Monitoring, functioning and control

**(a) Capabilities and limits in performance, incl. accuracy for specific persons or groups and overall expected accuracy**

- From readme.md "Known limitations": compensatory scores; cross-model score variance of 20+ points on the same input
  ("treat scores as bands ... treat the gate decision as the reliable signal"); topical-only pre-filter; no OCR (scanned
  resumes fail). No accuracy measured against real outcomes; no per-group accuracy. [TO FILL]

**(b) Foreseeable unintended outcomes and risks to health, safety, fundamental rights and discrimination**

- Visible from the design: wrongful rejection by an LLM-derived gate (severity chosen by the model); location, language
  proficiency and work-authorisation criteria can correlate with nationality or ethnic origin (indirect discrimination
  risk); "soft skills" and "education" ratings may reflect writing style or institution prestige; automatic rejection
  e-mails; model drift when `openrouter/auto` or env overrides change the model. [TO FILL] full risk analysis.

**(c) Human oversight measures needed (Art 14)**

- [TO FILL] (e.g. recruiter must review each gate rejection and each e-mail before sending; disable `--threshold`
  auto-decision wording).

**(d) Specifications on input data, as appropriate**

- Resume PDFs with embedded text (extraction shorter than 100 characters is rejected); job description as a text file;
  e-mail prompt uses the first 4,000 characters of the resume. [TO FILL] language support, maximum sizes.

## 4. Appropriateness of the performance metrics

**Why the chosen metrics fit this system**

- The current evals check bands and behaviours on 5 synthetic fixtures; LOOP.md itself states variance claims cannot be
  measured "at n=1 per cell" and plans a calibration fixture (C2b) and a labelled corpus (C8). [TO FILL] metrics that fit
  the intended purpose (e.g. agreement with human screeners, false-reject rate, group-wise rates).

## 5. Risk management system (Art 9)

**Detailed description of the risk management process**

- [TO FILL] (the gate design notes "FMEA severities" for gate questions; this is not a risk management system for the
  product).

## 6. Relevant changes made over the lifecycle

**Change log**

- LOOP.md "Done" section: 2026-08-26 eval harness and token-cost line; 2026-08-27 C1 gate with FMEA severities and
  default model changed to gpt-5.6-luna; 2026-08-28 C2 anchored scale with evidence before level; 2026-08-28 embedding
  pre-filter with content-keyed cache. The team should check that this list is complete.

## 7. Harmonised standards or other specifications applied

**List of standards / common specifications used, or other solutions**

- [TO FILL]

## 8. EU declaration of conformity (Art 47)

**Copy of the declaration**

- [TO FILL]

## 9. Post-market monitoring (Art 72)

**System to evaluate performance after release, incl. the monitoring plan**

- Only a per-run token/cost line and console output exist; no persistent decision logs (relevant to Art 12 as well).
  [TO FILL]

---
Coverage: 21 of 26 items have content from the code/docs; 9 still need the team ([TO FILL]), of which 5 have no content yet.

> Not legal advice. This is a readiness aid produced by software and an AI agent from the answers given. It can be wrong or incomplete, and the law and its guidance keep changing. Have a qualified lawyer confirm the classification and obligations before you rely on them.
