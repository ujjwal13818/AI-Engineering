import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from hello import greet


def test_greet():
    assert greet("Ujjwal") == "Hello, Ujjwal!"
