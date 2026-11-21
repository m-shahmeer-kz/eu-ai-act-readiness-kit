# Buyer test: expected answers (written BEFORE the agent ran)

Six real open-source AI products, cloned 21 Nov 2026 (commit in brackets). A fresh agent that never saw this
file runs the frozen skill v1.0.0 end to end on each, with no user available (so it must state assumptions).

| Repo | What it is | Expected category (my own reading of the AI Act) | Must-have in the agent's answer |
|---|---|---|---|
| srbhr/Resume-Matcher (959e458) | Self-hosted tool a **job seeker** uses to tailor their own resume to a job description with an LLM | Not high-risk: the candidate uses it for themselves, outside Annex III 4(a). Transparency only (AI-generated text, Art 50) | NOT high-risk; mentions 4(a) and why it is out |
| sliday/resume-job-matcher (9c06bb1) | CLI an **employer** runs to screen and rank resumes and decide who to interview | High-risk, Annex III 4(a), profiling, rules from 2 Dec 2027 | HIGH-RISK 4(a); Art 6(3) not available; Annex IV draft |
| mckaywrigley/chatbot-ui (81328b6) | Chat interface for LLMs | Transparency (Art 50(1) chatbot disclosure, Art 50(2) text marking) | Not high-risk; Art 50 duties that already apply |
| lllyasviel/Fooocus (ae05379) | Image generation app (Stable Diffusion XL) | Transparency: Art 50(2) machine-readable marking; deepfake labelling for deployers (Art 50(4)); safeguards against the new Art 5(1)(ba)/(bb) bans from 2 Dec 2026 | Not high-risk; Art 50(2); mentions the 2 Dec 2026 bans or marking date |
| kmhmubin/Face-Recognition-Attendance-System (0e87a9a) | Webcam face recognition that marks **students'** attendance for teachers | Borderline. Face identification against enrolled students, but people present themselves to the camera, so probably not *remote* (Annex III 1(a)); attendance is not a 3(a)-(d) education use. Most likely not high-risk, with a strong caveat and GDPR biometric-data warning | Must examine 1(a) remote vs verification/active involvement and flag the uncertainty; either answer is acceptable only if reasoned |
| max-fitzpatrick/Credit-scoring-model (fe92d9b) | Model predicting a **consumer's probability of default** (Kaggle "Give Me Some Credit") | High-risk, Annex III 5(b), profiling, if used for credit decisions about natural persons | HIGH-RISK 5(b) |
