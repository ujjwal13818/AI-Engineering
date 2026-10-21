user = {
    "name": "Ujjwal",
    "age": 24,
    "skills": ["Java", "Python"],
}

# Access
user["name"]                 # "Ujjwal"  (KeyError if the key is missing)
user.get("email")            # None      (safe, no error)
user.get("email", "n/a")     # "n/a"     (custom default)

# Modify
user["age"] = 25             # update
user["city"] = "Bengaluru"   # add
del user["city"]             # remove
user.pop("age")              # remove and return value

# Check
"name" in user               # True (checks keys)
len(user)                    # number of keys

# Loop
for key in user:                       # keys
    print(key)
for key, value in user.items():        # key and value together
    print(key, value)
user.keys(); user.values()

print(user.keys())


response = {
    "model": "some-llm",
    "choices": [
        {"message": {"role": "assistant", "content": "Hello!"}}
    ],
    "usage": {"input_tokens": 12, "output_tokens": 5},
}

text = response["choices"][0]["message"]["content"]   # "Hello!"
tokens = response["usage"]["output_tokens"]            # 5


messages = [
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "Explain RAG simply."},
]
messages.append({"role": "assistant", "content": "RAG is..."})

words = ["rag", "agent", "llm"]
lengths = {w: len(w) for w in words}      # {'rag': 3, 'agent': 5, 'llm': 3}

# Counting words, a very common task
from collections import Counter
counts = Counter("ai learns from data and ai uses data".split())
print(counts)                  # Counter({'ai': 2, 'data': 2, ...})
print(counts.most_common(2))   # [('ai', 2), ('data', 2)] 

import json
text = json.dumps(user)           # dict -> JSON string
data = json.loads(text)           # JSON string -> dict