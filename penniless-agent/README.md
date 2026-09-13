# XOOL Penniless Agent

Goal: earn the first £1 online with zero new spend, primarily through verifiable coding bounties.

This setup is adapted from the public `Echolonius/the-penniless-agent` field report. The original repo is a playbook/skill rather than a turnkey autonomous money-making program, so this folder turns its core rules into an automated bounty-hunting loop.

## What it does

- scans GitHub for open issues that appear to carry cash bounties
- extracts reward amounts when visible
- scores candidates for low competition
- rejects obvious weak signals where payment evidence is missing
- writes `bounty-report.md`
- can open/update a tracking issue when a promising candidate is found
- runs on a schedule with GitHub Actions

## First-£1 rule

Prioritize the smallest *credible and payable* task that can be completed quickly. £1 earned and received is more valuable for this experiment than a theoretical £1,000 bounty with 50 competing claims.

## Safety rules

Before work starts on a bounty:

1. Verify a real payment rail exists.
2. Prefer repositories/platforms with prior confirmed payouts.
3. Check whether the issue is already heavily claimed.
4. Check payout/KYC/region requirements before doing the work.
5. Never expose private keys, mnemonics, tokens, or `.env` files.
6. Do not spam maintainers or mass-claim issues.
7. Re-fetch any submitted PR/comment and verify it actually exists and passes CI.

## Limitation

The GitHub Action can discover and triage earning opportunities automatically. It cannot safely fork arbitrary third-party repositories, sign payout agreements, complete KYC, or accept financial terms on your behalf. When it finds a good target, the next step is to implement the fix and submit the PR from your GitHub identity.

Status: enabled for hourly scans and push-triggered scans.
