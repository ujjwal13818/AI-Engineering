from collections import Counter
import json

doc = {
    "title": "Learning Python",
    "author": "Alex",
    "tags": ["python", "learning", "beginner"],
    "word_count": 250,
}

print(doc["tags"][1])
print(doc.get("year", "unknown"))

messages = [
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "What is Python?"},
]
messages.append(
    {"role": "assistant", "content": "Python is a programming language."}
)

for message in messages:
    print(f"{message['role']}: {message['content']}")

sentences = [
    "AI learns from data.",
    "Robots can use AI.",
    "AI can answer questions.",
    "Machines can spot patterns.",
    "AI helps doctors.",
    "Chatbots use language models.",
    "AI can make predictions.",
    "People guide AI systems.",
]
word_counts = Counter(" ".join(sentences).lower().split())
print(word_counts.most_common(3))

json_string = json.dumps(doc, indent=2)
print(json_string)