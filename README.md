# ml-project-template
A modern, high-performance Machine Learning project skeleton. This template leverages `Hatchling` as the build backend and `uv` for lightning-fast dependency management and reproducibility

## Project Structure
```
my-ml-project/
├── .gitignore              # Keeps data, models, and venvs out of version control
├── pyproject.toml          # Build system, dependencies, and tool configs (Ruff, Pytest)
├── .pre-commit-config.yaml # Hooks for automatic linting and formatting on commit
├── README.md               # You are here!
├── uv.lock                 # Deterministic lockfile (COMMIT THIS to Git)
├── data/                   # Dataset storage (Git-ignored)
│   ├── raw/                # Original, immutable datasets
│   └── processed/          # Cleaned data ready for training
├── models/                 # Saved model weights/artifacts (Git-ignored)
├── notebooks/              # Prototyping & EDA (e.g., 01_initial_exploration.ipynb)
├── src/                    # The "Library": Reusable, versioned Python package
│   └── my_project/         # Source code (importable as 'import my_project')
│       ├── __init__.py
│       ├── preprocessing.py
│       └── training.py
├── tests/                  # Unit tests for your source code (via Pytest)
│   └── test_preprocessing.py 
```

- **`data/`**: Separated into `raw` and `processed`. Always treat raw data as read-only.
- **`models/`**: Stores serialized model artifacts. 
- **`src/`**: This is where stable code lives. If you write a great preprocessing function in a notebook, move it here so it can be tested and reused.
- **`notebooks/`**: Used for "scratchpad" work. Name them with numbers (e.g., `01-eda.ipynb`) to show the order of operations.

## Setup Instructions

1. **Install uv**: If not yet installed, run `curl -LsSf https://astral.sh/uv/install.sh | sh`
2. **Sync Environment**: Run the following to create a venv and install all dependencies:```uv sync --extra dev```
3. Run `uv run pre-commit install` to set up Ruff
4. Uncomment .gitignore file

**Confirm setup**

1. Initialize Git: Run `git init`.
2. Install dependencies: Run `uv sync --extra dev`.
3. Verify: Run `uv run pytest` to ensure environment is working and dev packages are installed (pytest should throw an import error).

## Workflow
This project uses Ruff for linting and formatting.

It runs every time you git commit. If it fails, it will fix the code; you just need to git add the changes and commit again. To check manually, run `uv run ruff check .` to check for errors or `uv run ruff format .` to fix spacing.

To use your project's environment and src code inside Jupyter: `uv run jupyter lab`. In a notebook cell, you can then import your logic: `from my_project.preprocessing import clean_data`.

IMPORTANT: never commit files inside `data/` or `models`; these are for local storage only. Move stable functions from notebooks into `src/main_project/` for better mainatainability.