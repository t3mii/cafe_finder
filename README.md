Poetry environment setup
========================

Quick steps to create and use a Poetry virtual environment for this project (PowerShell):

1. Install Poetry (if you don't have it):

   ```powershell
   (Invoke-WebRequest -Uri https://install.python-poetry.org -UseBasicParsing).Content | python -
   ```

2. Configure Poetry to create the virtualenv inside the project (recommended for VS Code) and install dependencies from `pyproject.toml`:

   ```powershell
   cd "c:\Users\grace\Coding Workspace\cafe_finder"
   poetry config virtualenvs.in-project true --local
   poetry env use python
   poetry install
   ```

3. Activate the environment for an interactive session or run a single command inside it:

   ```powershell
   poetry shell
   # or
   poetry run python main.py
   ```

Notes
- If you want VS Code to automatically use the environment created by Poetry, this project includes `.vscode/settings.json` which points the interpreter to `.venv/Scripts/python.exe`.
- Keep secrets out of the repo: put API keys in a `.env` file and it's already ignored by `.gitignore`.

Quick test
---------
There is a tiny `main.py` that prints the Python executable and a short list of installed packages to confirm the environment. Run:

```powershell
poetry run python main.py
```

Troubleshooting
---------------
- If `poetry env use python` fails, ensure the Python version you want is available on PATH (for example `python3.11` or the full path to the executable).
- To remove and recreate the venv: `poetry env remove <python>` then `poetry install`.

Further steps
-------------
- Add tests under a `tests/` folder and run `poetry run pytest`.
- Use `poetry add <package>` to add new dependencies and `poetry lock` to update `poetry.lock`.
