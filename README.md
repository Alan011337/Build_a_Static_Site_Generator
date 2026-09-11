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

## Learning context

This is a learning project completed while strengthening software-engineering fundamentals. It is not presented as a production CMS or framework.

The value of the project is the underlying implementation practice: file processing, content transformation, testing, build workflows, and reasoning about how a static-site pipeline works.

For broader product work, see my Haven portfolio:
https://somber-tamarillo-df3.notion.site/Haven-AI-native-Product-Portfolio-3d8ad9856018811b96ffe8e33a7d48ef
