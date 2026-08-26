---
name: xool-publishing-ops
description: Packages XOOL-approved Pinterest and social assets for publishing or scheduling with QA, filenames, captions, alt text, links, dates, platform notes, and execution safeguards.
---

# XOOL Publishing Operations

Prepare clean, auditable publishing handoffs.

## Inputs
Use only production-ready files from relevant `outputs/` folders plus:
- content calendar,
- compliance rules,
- platform/account mapping,
- approved destination links,
- scheduled dates and timezone.

## QA checklist
Verify:
- platform and format are correct,
- final copy matches the creative,
- destination link is correct,
- CTA is consistent with landing page,
- required disclaimer is present,
- no invented claim remains,
- asset ratio/resolution is appropriate,
- alt text is drafted where useful,
- campaign/test ID is recorded,
- account/board destination is correct,
- status is production-ready rather than draft.

## Output
Create `outputs/publishing/publishing-plan.md`:

```text
# XOOL Publishing Plan

| Date | Time | Platform | Board/Account | Asset | Copy | Destination | Test ID | Status | Notes |
|---|---|---|---|---|---|---|---|---|---|
```

## Execution authority
Preparing a publishing plan is allowed as internal work. Actual external publishing or scheduling requires the applicable execution authority or explicit user instruction.

Never store API keys or login credentials in the repository.
