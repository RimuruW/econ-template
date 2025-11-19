# Contributing Guide

Thank you for improving **econ-template**. This document describes how to set up your environment, propose changes, and keep discussions constructive. All contributors must also follow the [Code of Conduct](CODE_OF_CONDUCT.md).

## 1. Set Up a Reproducible Environment
1. Install system dependencies: Python 3.11+, R 4.3+, Quarto, `just`, `uv`, Git LFS.
2. Clone the repository and install hooks:
   ```bash
   git clone git@github.com:qingxu-code/econ-template.git
   cd econ-template
   just setup
   ```
   `just setup` installs Python packages via `uv`, restores the `renv` lockfile, configures Git LFS tracking, and enables `pre-commit` hooks.

## 2. Development Workflow
- Work on a dedicated branch (e.g., `feature/polars-upgrade` or `fix/report-theme`).
- Keep commits scoped and descriptive; reference related issues in the message body (e.g., `Fixes #12`).
- Run quality gates locally before every push:
  ```bash
  just check
  ```
  The target runs Ruff, pytest, and lintr to prevent regressions across languages.

## 3. Making Changes
1. **Discuss first**: open an issue (or comment on an existing one) for non-trivial changes to align on scope and design.
2. **Follow the project style**:
   - Prefer Python for heavy ETL steps; reserve R for modeling/visualization helpers.
   - Store reproducible scripts in `scripts/` or `src/py` / `src/r`; keep notebooks lightweight and data-backed.
   - Never commit sensitive data or credentials; reference reproducible download scripts instead.
3. **Document updates**: when behavior changes, update `README.md`, `template/README.md`, or Quarto docs so downstream template users understand the change.

## 4. Pull Request Checklist
- [ ] Branch is rebased on `master` with no merge commits.
- [ ] `just check` passes locally.
- [ ] Tests/notebooks demonstrating the change are included or updated.
- [ ] User-facing changes are documented (README, changelog, or inline comments).
- [ ] Large assets and generated reports are excluded from the diff.

## 5. Reporting Issues
Provide enough context for maintainers to reproduce the problem:
- Template hash (`git rev-parse HEAD`) and operating system.
- Exact command sequence (preferably `just …`).
- Observed output/logs and expected outcome.
- Whether the issue happens in the root template, a rendered project, or both.

## 6. Security and Responsible Disclosure
Do not open public issues for vulnerabilities that might expose private data pipelines. Instead, email `security@qingxu.dev` with a detailed report and reproduction steps. You will receive an acknowledgment within 5 business days.

## 7. Licensing
By submitting a contribution, you agree that it will be licensed under the MIT License that covers this repository. Ensure that any third-party code you include is also compatible with MIT terms.

We appreciate thoughtful PRs, even for documentation or examples. Thank you for helping keep econ-template reliable for the entire research community.
