def greet(name: str, excited: bool = False) -> str:
    """Return a greeting."""          # docstring: describes the function
    return f"Hello, {name}{'!' if excited else '.'}"

greet("Ujjwal")                  # "Hello, Ujjwal."
greet("Ujjwal", excited=True)  

print(greet("Ujjwal"))           # "Hello, Ujjwal."
print(greet("Ujjwal", excited=True))  # "Hello, Ujjwal!"

def build_prompt(question: str, tone: str = "simple", max_words: int = 100) -> str:
    return f"Answer in a {tone} tone, under {max_words} words: {question}"

print  (build_prompt("What is RAG?"))
print(build_prompt("What is RAG?", max_words=50))
print(build_prompt(question="What is RAG?", tone="formal"))

def top_words(text: str, n: int = 3) -> list[str]: ...
def count(words: list[str]) -> dict[str, int]: ...
def find(items: list[str], key: str) -> str | None: ...   # str or None


def add_all(*args):                  # args is a tuple
    return sum(args)

add_all(1, 2, 3)                     # 6

def show(**kwargs):                  # kwargs is a dict
    for key, value in kwargs.items():
        print(key, value)

show(model="some-llm", temperature=0.7)

config = {"tone": "formal", "max_words": 50}
build_prompt("What is RAG?", **config)     # same as passing tone=..., max_words=...

docs = [{"title": "A", "score": 0.4}, {"title": "B", "score": 0.9}]
best_first = sorted(docs, key=lambda d: d["score"], reverse=True)

def add_doc(doc, docs=[]):        # BAD: the same list is shared across calls
    docs.append(doc)
    return docs

def add_doc(doc, docs=None):      # GOOD
    if docs is None:
        docs = []
    docs.append(doc)
    return docs