# Write
with open("notes.txt", "w", encoding="utf-8") as f:
    f.write("RAG basics\n")
    f.write("Embeddings\n")

# Read the whole file
with open("notes.txt", "r", encoding="utf-8") as f:
    text = f.read()

# Read line by line (good for big files)
with open("notes.txt", encoding="utf-8") as f:
    for line in f:
        print(line.strip())

# Append
with open("notes.txt", "a", encoding="utf-8") as f:
    f.write("Agents\n")


import json

docs = [{"title": "A", "score": 0.4}, {"title": "B", "score": 0.9}]

with open("docs.json", "w", encoding="utf-8") as f:
    json.dump(docs, f, indent=2)          # dump/load work with files

with open("docs.json", encoding="utf-8") as f:
    loaded = json.load(f)                 # back to list of dicts


with open("data.jsonl", "w", encoding="utf-8") as f:
    for d in docs:
        f.write(json.dumps(d) + "\n")

with open("data.jsonl", encoding="utf-8") as f:
    rows = [json.loads(line) for line in f] 

from pathlib import Path

folder = Path("data")
folder.mkdir(exist_ok=True)  # create folder if it doesn't exist

file = folder / "notes.txt"
file.write_text("hello", encoding="utf-8")  # write text to file
print(file.read_text(encoding="utf-8"))  # read text from file
print(file.exists())

for p in folder.glob("*.txt"):     # find files by pattern
    print(p.name)

try:
    with open("missing.txt", encoding="utf-8") as f:
        text = f.read()
except FileNotFoundError:
    print("File not found, using empty text")
    text = ""

try:
    data = json.loads(raw)
    score = data["score"]
except json.JSONDecodeError:
    print("Not valid JSON")
except KeyError:
    print("No 'score' key")
except Exception as e:             # catch-all: use sparingly
    print(f"Unexpected error: {e}")
else:
    print("No error happened")
finally:
    print("Always runs")



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