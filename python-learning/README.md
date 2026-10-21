# Python Learning Environment

## Daily workflow
1. Open this folder in VS Code (`code .`).
2. Terminal -> New Terminal (venv activates automatically).
3. Run a script: `python src/hello.py`  (or press F5 to debug).
4. Run tests: `pytest` (or use the Testing panel).
5. Lint: `ruff check .`   Format: saved automatically via Black.

## Install a new package
    pip install <package>
    pip freeze > requirements.txt

## Recreate the environment elsewhere
    python -m venv .venv
    # Windows: .venv\Scripts\activate     macOS/Linux: source .venv/bin/activate
    pip install -r requirements.txt
