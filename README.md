# Python code template

## How to use
- Clone this project
- Change the git origin to your project `git remote set-url origin https://YOUR_ORG@dev.azure.com/YOUR_ORG/YOUR_PROJECT/_git/YOUR_REPO`. **This is very important!**
- Create a virtual environment for `Python>=3.7`, i.e. `python3 -m venv venv`
- Activate the new environment (`source venv/bin/activate` on Linux, `venv\Scripts\Activate.ps1` on Windows)
- Install development packages using `pip install -r requirements-test.txt`
- Install the pre-commti hook to the local git `pre-commit install`

## What's included
- Automated formatting & linting with `pre-commit` and VSCode
  - Formatting using `black` (settings in `pyproject.toml`)
  - Spell checks using `codespell` (settings in `.codespellrc`)
  - Linting using `ruff` (settings in `pyproject.toml`)
  - Import sort using `ruff` (settings in `pyproject.toml`)
- Tests using `pytest` (settings in `pyproject.toml`, also see `tests/README.md`)
  - Running pytest will generate a coverage report in `htmlcov`
- AutoDocstring generation extension in VSCode (best used for typed classes/methods)
- Ruff extension for VSCode for on-the-fly linting