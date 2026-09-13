#!/usr/bin/env python3
"""XOOL Penniless Agent bounty scanner.

Uses GitHub Search API only; no third-party packages required.
Writes a ranked Markdown report to penniless-agent/bounty-report.md.
"""

from __future__ import annotations

import json
import os
import re
import sys
import urllib.parse
import urllib.request
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path

TOKEN = os.environ.get("GITHUB_TOKEN", "")
API = "https://api.github.com"
REPORT = Path(__file__).with_name("bounty-report.md")

SEARCHES = [
    'is:issue is:open label:"💎 Bounty"',
    'is:issue is:open label:bounty',
    'is:issue is:open in:title bounty',
]

MONEY_RE = re.compile(r"(?:\$|USD\s?|USDC\s?|£)\s?([0-9][0-9,]*(?:\.\d{1,2})?)", re.I)


@dataclass
class Candidate:
    repo: str
    number: int
    title: str
    url: str
    comments: int
    created_at: str
    amount: float | None
    currency_hint: str | None
    body: str
    score: float = 0.0


def gh_get(path: str) -> dict:
    req = urllib.request.Request(API + path)
    req.add_header("Accept", "application/vnd.github+json")
    req.add_header("X-GitHub-Api-Version", "2022-11-28")
    req.add_header("User-Agent", "xool-penniless-agent")
    if TOKEN:
        req.add_header("Authorization", f"Bearer {TOKEN}")
    with urllib.request.urlopen(req, timeout=30) as r:
        return json.load(r)


def parse_amount(text: str) -> tuple[float | None, str | None]:
    if not text:
        return None, None
    m = MONEY_RE.search(text)
    if not m:
        return None, None
    raw = m.group(0)
    amount = float(m.group(1).replace(",", ""))
    if "£" in raw:
        cur = "GBP"
    elif "USDC" in raw.upper():
        cur = "USDC"
    else:
        cur = "USD"
    return amount, cur


def score(c: Candidate) -> float:
    # First £1 experiment: small-but-real, low-competition tasks rank highly.
    s = 100.0
    s -= min(c.comments * 6.0, 60.0)
    if c.amount is None:
        s -= 25
    else:
        if 1 <= c.amount <= 50:
            s += 20
        elif 50 < c.amount <= 250:
            s += 10
        elif c.amount > 1000:
            s -= 10
    text = (c.title + "\n" + c.body).lower()
    if any(k in text for k in ("good first issue", "docs", "documentation", "test", "typo", "ci", "lint")):
        s += 12
    if any(k in text for k in ("security", "exploit", "pentest", "kyc", "region restricted")):
        s -= 18
    if c.comments == 0:
        s += 10
    return round(s, 1)


def main() -> int:
    seen: dict[str, Candidate] = {}
    for q in SEARCHES:
        query = urllib.parse.urlencode({"q": q, "sort": "created", "order": "desc", "per_page": 50})
        try:
            data = gh_get("/search/issues?" + query)
        except Exception as e:
            print(f"search failed: {q}: {e}", file=sys.stderr)
            continue
        for item in data.get("items", []):
            if "pull_request" in item:
                continue
            repo_url = item.get("repository_url", "")
            repo = repo_url.rsplit("/", 2)[-2] + "/" + repo_url.rsplit("/", 1)[-1] if repo_url else "unknown"
            body = item.get("body") or ""
            amount, cur = parse_amount((item.get("title") or "") + "\n" + body)
            c = Candidate(
                repo=repo,
                number=int(item["number"]),
                title=item.get("title") or "",
                url=item.get("html_url") or "",
                comments=int(item.get("comments") or 0),
                created_at=item.get("created_at") or "",
                amount=amount,
                currency_hint=cur,
                body=body[:3000],
            )
            c.score = score(c)
            seen[c.url] = c

    ranked = sorted(seen.values(), key=lambda c: (c.score, -(c.amount or 0)), reverse=True)
    now = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")

    lines = [
        "# XOOL Penniless Agent — Bounty Report",
        "",
        f"Updated: **{now}**",
        "",
        "Mission: find the fastest credible route to the first **£1 actually received**.",
        "",
        "## Top candidates",
        "",
        "| Score | Reward | Competition | Repository | Issue |",
        "|---:|---:|---:|---|---|",
    ]
    for c in ranked[:20]:
        reward = "unknown"
        if c.amount is not None:
            sym = "£" if c.currency_hint == "GBP" else "$"
            reward = f"{sym}{c.amount:g}"
        title = c.title.replace("|", "\\|")
        lines.append(f"| {c.score:.1f} | {reward} | {c.comments} comments | `{c.repo}` | [{title}]({c.url}) |")

    lines += [
        "",
        "## Agent decision rule",
        "",
        "Before coding, manually verify the top candidate has a real funded/rewarded bounty and prior payout evidence. Do not work from the dollar amount in a title alone.",
        "",
        "The scanner is intentionally conservative: it optimizes for *probability of first payment*, not headline bounty size.",
        "",
    ]
    REPORT.write_text("\n".join(lines), encoding="utf-8")

    if ranked:
        best = ranked[0]
        print(json.dumps({
            "best_url": best.url,
            "best_title": best.title,
            "best_repo": best.repo,
            "best_score": best.score,
            "best_comments": best.comments,
            "best_amount": best.amount,
            "best_currency": best.currency_hint,
        }))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
