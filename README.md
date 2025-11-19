# Econ Template

A reproducible research template that combines Python, R, Quarto, and Just to standardize applied economics projects. Use it to spin up a clean codebase, enforce data-handling discipline, and keep empirical workflows auditable from day one.

## Why This Template

- **Hybrid workflow**: Python handles heavy data engineering while R focuses on modeling and graphics.
- **Deterministic builds**: `uv`, `renv`, and Just targets capture every dependency and command.
- **Publication ready**: Quarto reports live next to your data pipeline, figures, and tables.
- **Data hygiene**: Opinionated directory layout keeps raw, interim, and processed assets separated and versioned correctly.

## Getting Started

1. Install prerequisites: Python 3.11+, R 4.3+, Quarto, `just`, `uv`, and Git LFS.
2. Generate a project: `copier copy gh:RimuruW/econ-template <your-project-name>`.
3. Enter the new directory and run `just setup` to install Python/R deps, configure pre-commit, and enable Git LFS.
4. Develop iteratively: orchestrate pipelines with `just all` or call individual tasks such as `just data-fetch`, `just data-clean`, `just report`.
5. Run `just check` before every commit; it executes Ruff, pytest, and lintr to guard regressions.

## Repository Layout

```
template/
├─ config/ project-wide settings
├─ data/   staged storage for raw→interim→processed assets
├─ notebooks/ exploratory analysis in Python, R, and Quarto
├─ reports/ publication sources
├─ scripts/ numbered pipeline steps
├─ src/     reusable Python + R modules
└─ tests/   unit and integration coverage
```

`generated-demo/` is a fully materialized example of the template outcome; `copier.yml` defines the rendering prompts.

## Usage Guidance

- Treat `data/raw` as read-only input; regenerated artifacts belong in `data/interim` and `data/processed` and remain gitignored.
- Commit Quarto sources, not rendered PDFs. Use `just report` when you need artifacts.
- Keep credentials outside the repo; placeholders exist under `config/` and `.env` for local overrides only.
- Prefer Parquet for tabular outputs and 300 DPI PNG for graphics to ensure consistent downstream use.

## Open Collaboration

- License: MIT. Reference it when publishing derived work and keep attribution for bundled assets.
- Issues: file reproducible bug reports or feature proposals before opening a pull request.
- Pull requests: include tests or notebooks that demonstrate behavior; describe any data assumptions or privacy constraints.
- Data policy: never commit proprietary or unreproducible raw data—store pointers or scripts that re-fetch them instead.

## Maintenance Checklist

- Run `just snapshot` whenever dependency pins change (`uv.lock`, `renv.lock`).
- Sync Quarto extensions via `just report --to html` if upstream templates evolve.
- Periodically update Copier by rerendering in a scratch directory and diffing against this repo to keep prompts current.

Build on top of this template, but keep it lean: remove components you do not need and document any project-specific conventions directly in the generated project.
