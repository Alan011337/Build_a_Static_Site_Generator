# Static Site Generator in Python

A learning project for building a small static-site generator from first principles in Python.

The project turns source content into generated HTML using a template-based build pipeline, with scripts for building, running, and testing the site.

## What this project demonstrates

- Working with files and directories in Python
- Parsing and transforming content into HTML
- Separating source content, static assets, templates, and generated output
- Building a repeatable generation workflow
- Writing tests around content-processing logic
- Using shell scripts to standardize common project commands

## Pipeline at a glance

```text
Source content
   ↓
Parse / transform
   ↓
Template composition
   ↓
Generated HTML
   ↓
Static output (`docs/`)
```

The useful implementation idea is the separation between **source-of-truth content**, **transformation logic**, **presentation template**, and **generated artifact**. That separation makes the workflow easier to reason about, test, and rebuild.

## Project structure

```text
.
├── content/        # source content
├── static/         # static assets
├── src/            # Python implementation
├── docs/           # generated site output
├── template.html   # page template
├── build.sh        # build workflow
├── main.sh         # local run workflow
└── test.sh         # test workflow
```

## Why this matters for product / technical work

A static-site generator is small, but it exposes several concepts that recur in larger software systems:

- **Source vs. rendered state:** generated output should not become the canonical truth.
- **Transformation boundaries:** parsing, conversion, templating, and output generation are separate responsibilities.
- **Repeatability:** the build should be reproducible instead of relying on manual page editing.
- **Testability:** content-processing logic can be checked independently from visual output.
- **Failure localization:** when an output is wrong, the issue may be in source content, parser logic, template composition, or build orchestration.

For a Product / TPM context, this is useful evidence that I can reason about a transformation pipeline and distinguish canonical inputs from derived artifacts — a pattern that also matters in documentation systems, content products, data pipelines, and AI-assisted generation workflows.

## Reviewer guide

A useful discussion of this repository should be able to answer:

1. What is the canonical source of truth, and what is generated state?
2. Why separate parsing / transformation from template rendering?
3. Where should tests sit in the pipeline?
4. If generated HTML is wrong, how would you isolate the failure?
5. What changes would be needed before treating this as a production content platform?

## Evidence boundary

This repository supports claims about Python program structure, file/content transformation, repeatable build workflows, and basic testing discipline. It does **not** by itself establish production CMS ownership, large-scale frontend architecture, deployment-platform expertise, or web-product traffic at scale.

## Learning context

This is a learning project completed while strengthening software-engineering fundamentals. It is not presented as a production CMS or framework.

The value of the project is the underlying implementation practice: file processing, content transformation, testing, build workflows, and reasoning about how a static-site pipeline works.

For broader product work, see my Haven portfolio:
https://somber-tamarillo-df3.notion.site/Haven-AI-native-Product-Portfolio-3d8ad9856018811b96ffe8e33a7d48ef
