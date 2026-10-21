from pathlib import Path

folder = Path("data")
folder.mkdir(exist_ok=True)  # create folder if it doesn't exist

file = folder / "notes.txt" 

with open(file, "w" , encoding = "utf-8") as f:
    f.write("HELLO\n")
    f.write("WORLD\n")
    f.write("PYTHON\n")

with open(file, encoding="utf-8") as f:
    lines = f.read().splitlines()     # ['HELLO', 'WORLD', 'PYTHON']

for line in reversed(lines):
    print(line)

import json

scorecard = [{"title": "A", "score": 0.4}, {"title": "B", "score": 0.9}, {"title": "C", "score": 0.7}]
with open("data/scorecard.json", "w", encoding="utf-8") as f:
    json.dump(scorecard, f, indent=2)          # dump/load work with files      

with open("data/scorecard.json", encoding="utf-8") as f:
    loaded = json.load(f)                 # back to list of dicts
    max_score = max(d["score"] for d in loaded)
    print(next(d["title"] for d in loaded if d["score"] == max_score))

with open("data/scorecard.jsonl", "w", encoding="utf-8") as f:
    for d in scorecard:
        f.write(json.dumps(d) + "\n")

with open("data/scorecard.jsonl", encoding="utf-8") as f:
    lines = f.read().splitlines()

for line in reversed(lines):
    data = json.loads(line)
    print(data["title"], data["score"])

def  safe_load(path: str) -> list[dict]:
    try:
        with open(path, encoding = "utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"File {path} not found, returning empty list")
        return []
    except json.JSONDecodeError:
        print(f"File {path} is not valid JSON, returning empty list")
        return []

safe_load("data/scorecard.json")
safe_load("data/missing.json")
safe_load("data/invalid.json")  # assuming this file has invalid JSON


import time

def call_with_retry(fn, retries: int = 3):
    for attempt in range(1, retries + 1):
        try:
            return fn()
        except Exception as e:
            print(f"Attempt {attempt} failed: {e}")
            if attempt == retries:
                raise                      # give up, pass the error on
            time.sleep(2 ** attempt)       # wait 2s, 4s, ...


flaky_calls = [0]

def flaky():
    flaky_calls[0] += 1
    if flaky_calls[0] < 3:
        raise RuntimeError(f"temporary failure on call {flaky_calls[0]}")
    return f"Succeeded on attempt {flaky_calls[0]}"

print(call_with_retry(flaky))