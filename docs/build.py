"""Build docs/index.html from results/*.json so every number on the page is a measured one.

Run:  python docs/build.py
"""
import html
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
HOLD = json.loads((ROOT / "results" / "holdout_blind_results.json").read_text())
DEV = json.loads((ROOT / "results" / "dev_results.json").read_text())
BUYER = json.loads((ROOT / "results" / "buyer_test.json").read_text())
AGENSI_URL = "https://www.agensi.io/creators/muhammad-shahmeer"  # storefront; swap for the direct listing URL once approved
PRICE = "$29"
GH = "https://github.com/m-shahmeer-kz/eu-ai-act-readiness-kit"
e = html.escape

hs, ds = HOLD["summary"], DEV["summary"]
reason_diff = sum(1 for r in HOLD["rows"] if r["verdict_ok"] and r["official"] == "not" and not r["reason_ok"])
not_ok = hs["not_high_risk_cases"] - hs["false_alarms"]

buy = f'<a class="btn solid" href="{AGENSI_URL}" target="_blank" rel="noopener">Get it on Agensi · {PRICE} ↗</a>'

wrong_rows = "".join(
    f"<tr><td>{e(r['id'])}</td><td>{e(r['point'])}</td><td>{e(r['description'])}</td><td>not high-risk</td><td>high-risk</td></tr>"
    for r in HOLD["rows"] if not r["verdict_ok"])
area_rows = "".join(f"<tr><td>{e(a)}</td><td>{e(v)}</td></tr>" for a, v in hs["by_area"].items())
dev_area_rows = "".join(f"<tr><td>{e(a)}</td><td>{e(v)}</td></tr>" for a, v in ds["by_area"].items())
buyer_rows = "".join(
    f"<tr><td><a href=\"{e(b['url'])}\">{e(b['repo'])}</a></td><td>{e(b['what'])}</td><td>{e(b['expected'])}</td>"
    f"<td>{e(b['skill'])}</td><td>{'✅' if b['match'] else '⚠️'} {e(b['note'])}</td></tr>" for b in BUYER["projects"])

page = f"""<!DOCTYPE html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>EU AI Act Readiness Kit · is your AI product high-risk?</title>
<meta name="description" content="AI-agent skill that checks an AI product against the EU AI Act: risk category, obligations with dates, Annex IV technical documentation draft. Updated for the 2026 Digital Omnibus. Blind-tested on the Commission's own examples. Not legal advice.">
<meta property="og:type" content="website">
<meta property="og:title" content="EU AI Act Readiness Kit · is your AI product high-risk?">
<meta property="og:description" content="Risk category, obligations with dates and an Annex IV documentation draft, from your AI agent. Blind-tested on the European Commission's own examples. Not legal advice.">
<meta property="og:url" content="https://m-shahmeer-kz.github.io/eu-ai-act-readiness-kit/">
<meta property="og:image" content="https://m-shahmeer-kz.github.io/eu-ai-act-readiness-kit/assets/og.png">
<meta property="og:image:width" content="1200"><meta property="og:image:height" content="627">
<meta name="twitter:card" content="summary_large_image">
<link rel="icon" href="assets/logo.png">
<style>
:root{{--bg:#060607;--card:#111113;--line:#26262b;--text:#f2f2f3;--mute:#9a9aa2;--ok:#7ee2a8;--bad:#ff8a8a;--warn:#ffd27a}}
*{{box-sizing:border-box}}html{{-webkit-text-size-adjust:100%}}
body{{margin:0;background:var(--bg);color:var(--text);font:15px/1.6 system-ui,-apple-system,"Segoe UI",Roboto,sans-serif}}
.wrap{{max-width:1040px;margin:0 auto;padding:40px 20px 70px}}
h1{{font-size:clamp(32px,5.4vw,52px);line-height:1.04;margin:0 0 12px;letter-spacing:-.025em}}
h2{{font-size:clamp(20px,3vw,27px);margin:48px 0 10px;letter-spacing:-.01em}}
p,li{{color:#d6d6da}}.sub{{color:var(--mute);max-width:820px}}a{{color:var(--text)}}
code{{font:13px ui-monospace,SFMono-Regular,Menlo,monospace;background:#17171a;border:1px solid var(--line);border-radius:5px;padding:1px 5px;overflow-wrap:anywhere}}
.grid{{display:grid;grid-template-columns:repeat(auto-fit,minmax(220px,1fr));gap:12px}}
.card{{background:var(--card);border:1px solid var(--line);border-radius:16px;padding:16px 18px}}
.card h3{{margin:0 0 6px;font-size:16px}}.card p{{margin:0;font-size:14px}}
.stat b{{display:block;font-size:30px;line-height:1.1}}.stat span{{color:var(--mute);font-size:13px}}
.notice{{border:1px solid var(--warn);color:var(--warn);border-radius:14px;padding:12px 16px;margin:18px 0;font-size:14px}}
.tbl{{overflow-x:auto}}table{{border-collapse:collapse;width:100%;font-size:14px;margin:10px 0}}
th,td{{border-bottom:1px solid var(--line);padding:8px;text-align:left;vertical-align:top}}th{{color:var(--mute);font-weight:500}}
.btns{{display:flex;flex-wrap:wrap;gap:8px;margin:16px 0}}
.btn{{display:inline-block;padding:10px 18px;border:1px solid var(--line);border-radius:999px;text-decoration:none;font-size:14px}}
.btn.solid{{background:var(--text);color:#000;border-color:var(--text);font-weight:600}}
.steps{{counter-reset:s;list-style:none;padding:0}}.steps li{{counter-increment:s;margin:8px 0;padding-left:34px;position:relative}}
.steps li:before{{content:counter(s);position:absolute;left:0;top:1px;width:24px;height:24px;border-radius:50%;border:1px solid var(--line);text-align:center;font-size:13px;line-height:23px;color:var(--mute)}}
.time{{border-left:2px solid var(--line);margin:10px 0 0 6px;padding-left:16px}}.time p{{margin:6px 0}}.time b{{color:var(--text)}}
details summary{{cursor:pointer;color:var(--mute)}}
</style></head>
<body><div class="wrap">
<p class="sub" style="letter-spacing:.12em;text-transform:uppercase;font-size:12px">AI-agent skill · Claude Code · Codex · Cursor · Gemini CLI</p>
<h1>Is your AI product high-risk under the EU AI Act?</h1>
<p class="sub">EU AI Act Readiness Kit lets your AI coding agent check an AI product against the EU AI Act. It scans the code for AI use,
works out the risk category with the articles behind it, lists every obligation that applies with its date and the days left,
and drafts the paperwork: the Annex IV technical documentation, the Article 6(3) record, transparency notices and an AI literacy plan.
Built on the law as amended by the 2026 Digital Omnibus (Regulation (EU) 2026/1744).</p>
<div class="notice"><b>Not legal advice.</b> This is a readiness aid. It can be wrong, and the law and its guidance are still changing.
Every report says so and asks you to have a qualified lawyer confirm the result before you rely on it.</div>
<div class="btns">{buy}<a class="btn" href="#tested">Blind test results</a><a class="btn" href="#dates">Key dates</a><a class="btn" href="{GH}">GitHub ↗</a></div>

<h2 id="tested">Tested on the European Commission's own examples</h2>
<p class="sub">In May 2026 the Commission published draft guidelines with hundreds of practical examples of AI systems that should or should
not count as high-risk. I collected {len(HOLD['rows']) + len(DEV['rows'])} of them from the official AI Act Service Desk and split them by area.
I built the skill on four areas only. Then I froze it and gave the other {hs['cases']} examples (education, essential services and credit,
migration, justice and elections, and cross-cutting cases) to a fresh AI agent that had never seen them or their answers. It followed the skill once.</p>
<div class="grid">
 <div class="card stat"><b>{hs['verdict_correct']} / {hs['cases']}</b><span>correct high-risk / not-high-risk verdicts in the blind test ({round(hs['accuracy']*100)}%)</span></div>
 <div class="card stat"><b>{hs['high_risk_caught']} / {hs['high_risk_cases']}</b><span>high-risk systems recognised: none missed</span></div>
 <div class="card stat"><b>{hs['false_alarms']} / {hs['not_high_risk_cases']}</b><span>not-high-risk systems wrongly flagged as high-risk (all errors were on the cautious side)</span></div>
 <div class="card stat"><b>{ds['verdict_correct']} / {ds['cases']}</b><span>on the four development areas (employment, biometrics, critical infrastructure, law enforcement), used to build the skill</span></div>
</div>
<details><summary>The {hs['false_alarms']} blind-test mistakes</summary>
<div class="tbl"><table><tr><th>Case</th><th>Point</th><th>Example (Commission, paraphrased)</th><th>Commission</th><th>Skill</th></tr>{wrong_rows}</table></div></details>
<details><summary>Results by area</summary>
<div class="tbl"><table><tr><th>Blind test area</th><th>Correct</th></tr>{area_rows}</table>
<table><tr><th>Development area</th><th>Correct</th></tr>{dev_area_rows}</table></div></details>
<p class="sub">Honest notes: the examples are short paraphrases of the Commission's draft guidelines, which are not final and not binding.
In {reason_diff} of the {not_ok} correct "not high-risk" answers, the skill gave a different reason than the Commission
("outside the use case" versus "Article 6(3) exemption"). That matters because the exemption must be documented and registered.
This test covers the high-risk decision only; prohibited practices, transparency duties, GPAI rules and dates are covered by {BUYER['unit_tests']} automated tests.</p>

<h2>Buyer test on six real open-source AI products</h2>
<p class="sub">A separate fresh agent installed the frozen skill and ran it end to end on six real GitHub projects, with nobody to answer its questions.
I wrote down my expected answer for each project before it ran.</p>
<div class="tbl"><table><tr><th>Project</th><th>What it is</th><th>Expected</th><th>Skill's result</th><th>Match</th></tr>{buyer_rows}</table></div>
<p class="sub">{e(BUYER['summary'])}</p>

<h2>What your agent does with it</h2>
<ol class="steps">
<li>Scans the codebase for AI use: model libraries, calls to OpenAI, Anthropic, Gemini, Mistral and others, face and voice biometrics, emotion recognition, chat interfaces, generated media, with file and line.</li>
<li>Fills a structured questionnaire from the code, the docs and your answers: role (provider or deployer), intended purpose, company size.</li>
<li>Checks all 10 prohibited practices, including the two new bans from 2 December 2026, then the high-risk routes (Annex I products, Annex III use cases), the Article 6(3) exemption and profiling, transparency duties and general-purpose AI rules.</li>
<li>Writes a report: risk category with articles, every obligation with who, what, the date and the days left, penalties and key dates.</li>
<li>Drafts documents: Annex IV technical documentation (9 sections, prefilled from the code where possible), Article 6(3) assessment record, transparency notices, safeguards record for generators, AI literacy plan.</li>
<li>Answers you in plain English: what applies now, what comes next, the first actions, and the open questions. Always with the not-legal-advice note.</li>
</ol>

<h2 id="dates">Key dates after the 2026 Digital Omnibus</h2>
<div class="time">
<p><b>2 Feb 2025</b> Prohibited practices banned; AI literacy duty.</p>
<p><b>2 Aug 2025</b> General-purpose AI model rules.</p>
<p><b>2 Aug 2026</b> Transparency duties: tell people they talk to AI, mark AI-generated content, label deepfakes.</p>
<p><b>2 Dec 2026</b> New bans on AI that makes non-consensual intimate imagery or child sexual abuse material; generators already on the market must mark outputs.</p>
<p><b>2 Dec 2027</b> High-risk rules for Annex III use cases (hiring, education, credit, insurance, biometrics...).</p>
<p><b>2 Aug 2028</b> High-risk rules for AI in regulated products (medical devices, toys, lifts...).</p>
</div>

<h2>Good to know</h2>
<div class="grid">
 <div class="card"><h3>Who it is for</h3><p>European start-ups and agencies that build AI products and want to know where they stand before customers, investors or authorities ask.</p></div>
 <div class="card"><h3>Small install</h3><p>One Python script, standard library only (Python 3.10+). Nothing leaves your machine.</p></div>
 <div class="card"><h3>Conservative by design</h3><p>When a deciding fact is unknown, it asks and assumes the stricter reading. In the blind test every error was a false alarm, never a miss.</p></div>
 <div class="card"><h3>Honest limits</h3><p>It does not cover GDPR, copyright, product liability or sector law, and it cannot replace a lawyer. The law version is printed on every report.</p></div>
</div>

<div class="btns" style="margin-top:34px">{buy}<a class="btn" href="{GH}">GitHub ↗</a></div>
<p class="sub">Made by <a href="https://m-shahmeer-kz.github.io/">Muhammad Shahmeer</a> · Data Science MSc, University of Naples Federico II · © 2026, all rights reserved.
Not legal advice. Not affiliated with the European Commission. Examples paraphrased from the Commission's draft guidelines (AI Act Service Desk).</p>
</div></body></html>
"""
(ROOT / "docs" / "index.html").write_text(page)
print("wrote docs/index.html", len(page))
