# Automation & AI Toolkit

A public toolkit for reproducible automation workflows.

## Current working MVP

The included workflow runner can:
- replace text
- run regular-expression transformations
- add prefixes/suffixes
- process files through a JSON-defined pipeline

```bash
python workflow_runner.py example_workflow.json sample.txt
```

## AI Integration Policy

This starter intentionally includes **no embedded API key and no hard-coded external AI provider**.

Future provider adapters should:
- read credentials from protected environment variables
- keep prompts and data classification explicit
- avoid sending confidential client data by default
- log only publication-safe metadata
- support a local/dry-run mode

This keeps the public repository useful without pretending an external AI integration is already deployed.
