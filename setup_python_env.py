#!/usr/bin/env python3
"""
Bootstraps a Python learning environment for VS Code.

Usage:
    python setup_python_env.py [project_name]

Creates:
    <project_name>/
        .venv/                  virtual environment
        .vscode/settings.json   interpreter, formatting, testing
        .vscode/extensions.json recommended extensions
        .vscode/launch.json     debug config
        src/hello.py            first script
        tests/test_hello.py     first pytest test
        notebooks/              for Jupyter experiments
        requirements.txt
        .gitignore
        README.md
"""
import json
import subprocess
import sys
import venv
from pathlib import Path

PROJECT = sys.argv[1] if len(sys.argv) > 1 else "python-learning"
ROOT = Path(PROJECT).resolve()

REQUIREMENTS = """\
pytest
ruff
black
ipykernel
jupyter
rich
requests
"""

SETTINGS = {
    "python.defaultInterpreterPath": "${workspaceFolder}/.venv/Scripts/python.exe"
    if sys.platform == "win32"
    else "${workspaceFolder}/.venv/bin/python",
    "python.terminal.activateEnvironment": True,
    "python.testing.pytestEnabled": True,
    "python.testing.pytestArgs": ["tests"],
    "editor.formatOnSave": True,
    "[python]": {"editor.defaultFormatter": "ms-python.black-formatter"},
    "editor.rulers": [88],
    "files.autoSave": "afterDelay",
    "notebook.formatOnSave.enabled": True,
}

EXTENSIONS = {
    "recommendations": [
        "ms-python.python",
        "ms-python.vscode-pylance",
        "ms-python.black-formatter",
        "charliermarsh.ruff",
        "ms-toolsai.jupyter",
    ]
}

LAUNCH = {
    "version": "0.2.0",
    "configurations": [
        {
            "name": "Python: Current File",
            "type": "debugpy",
            "request": "launch",
            "program": "${file}",
            "console": "integratedTerminal",
        }
    ],
}

HELLO = '''\
def greet(name: str) -> str:
    return f"Hello, {name}!"


def main() -> None:
    print(greet("Python"))


if __name__ == "__main__":
    main()
'''

TEST_HELLO = '''\
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from hello import greet


def test_greet():
    assert greet("Ujjwal") == "Hello, Ujjwal!"
'''

GITIGNORE = """\
.venv/
__pycache__/
*.pyc
.pytest_cache/
.ruff_cache/
.ipynb_checkpoints/
.DS_Store
"""

README = """\
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
    # Windows: .venv\\Scripts\\activate     macOS/Linux: source .venv/bin/activate
    pip install -r requirements.txt
"""


def write(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")


def main() -> None:
    if sys.version_info < (3, 9):
        sys.exit("Python 3.9+ required.")

    print(f"Creating project at {ROOT}")
    ROOT.mkdir(parents=True, exist_ok=True)
    (ROOT / "notebooks").mkdir(exist_ok=True)

    write(ROOT / "requirements.txt", REQUIREMENTS)
    write(ROOT / ".gitignore", GITIGNORE)
    write(ROOT / "README.md", README)
    write(ROOT / "src" / "hello.py", HELLO)
    write(ROOT / "tests" / "test_hello.py", TEST_HELLO)
    write(ROOT / ".vscode" / "settings.json", json.dumps(SETTINGS, indent=4))
    write(ROOT / ".vscode" / "extensions.json", json.dumps(EXTENSIONS, indent=4))
    write(ROOT / ".vscode" / "launch.json", json.dumps(LAUNCH, indent=4))

    print("Creating virtual environment (.venv)...")
    venv.create(ROOT / ".venv", with_pip=True)
    py = ROOT / ".venv" / ("Scripts" if sys.platform == "win32" else "bin") / (
        "python.exe" if sys.platform == "win32" else "python"
    )

    print("Installing packages...")
    subprocess.check_call([str(py), "-m", "pip", "install", "--upgrade", "pip"])
    subprocess.check_call([str(py), "-m", "pip", "install", "-r", str(ROOT / "requirements.txt")])

    print("Running sample test...")
    subprocess.call([str(py), "-m", "pytest", "-q"], cwd=ROOT)

    print(f"\nDone. Next:\n  cd {PROJECT}\n  code .")
    print("Then accept the 'install recommended extensions' prompt in VS Code.")


if __name__ == "__main__":
    main()
