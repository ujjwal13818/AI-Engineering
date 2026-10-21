from collections import Counter


def build_prompt(question: str, tone: str, max_words: int) -> str:
    return f"Answer in a {tone} tone, under {max_words} words: {question}"


def top_words(text: str, n: int = 3) -> list[str]:
    words = text.lower().replace(".", "").replace(",", "").split()
    return [word for word, count in Counter(words).most_common(n)]

def make_message(role: str, content: str) -> dict[str, str]:
    return {"role": role, "content": content}

def log(*args, **kwargs) -> None:
    print(*args, **kwargs)

def sortDict(docs: list[dict], key: str, reverse: bool = False) -> list[dict]:
    return sorted(docs, key=lambda d: d[key], reverse=reverse)


print(build_prompt("What is RAG?", "simple", 100))
print(build_prompt("What is RAG?", "complex", 500))
print(build_prompt("What is RAG?", "formal", 100))

sample_text = "Python is fun, and Python is useful. Learning Python is fun."
print(top_words(sample_text))

make_message("user", "What is RAG?")
make_message("assistant", "RAG is Retrieval-Augmented Generation.")

log(("model", "some-llm"), ("temperature", 0.7))

sorted_docs = sortDict([{"name": "Alice", "age": 30}, {"name": "Bob", "age": 25}], "age")
print(sorted_docs)  # [{'name': 'Bob', 'age': 25}, {'name': 'Alice', 'age': 30}]