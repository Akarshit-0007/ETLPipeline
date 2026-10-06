# ETLPipeline

ETLPipeline is a Python-based web data extraction project designed around the Extract, Transform, Load workflow. It uses Playwright for browser automation, Pandas for data processing, Apache Airflow for scheduling, and PostgreSQL for persistent storage.

The repository currently contains a working Playwright smoke test in `main.py`. It launches Chromium, opens Google, waits briefly, and prints the page title. The remaining modules are intended as the foundation for a complete ETL pipeline: `src/scraper.py` for extraction, `src/models.py` for data models, `src/databse.py` for database operations, and `dags/scraping_dag.py` for Airflow orchestration.

## Setup

Install the project dependencies with:

```bash
uv sync
```

Install the Chromium browser for Playwright:

```bash
uv run playwright install chromium
```

## Run

```bash
uv run main.py
```

The current script should display a confirmation that Google loaded successfully. The Airflow DAG, database integration, and data transformation code are not yet implemented.

## Requirements

Python 3.14 or newer is required. The project dependencies are defined in `pyproject.toml`.
