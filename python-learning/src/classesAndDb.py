class Chatbot: #data + behaviour state.
    def __init__(self, name: str, model: str = "some-llm"):   # constructor
        self.name = name                                      # instance fields
        self.model = model
        self.history: list[dict[str, str]] = []

    def add_message(self, role: str, content: str) -> None:
        self.history.append({"role": role, "content": content})

    def turns(self) -> int:
        return len(self.history)

bot = Chatbot("helper")            # no `new` keyword
bot.add_message("user", "Hi")
print(bot.turns())  
print(bot.history)               # 1


from dataclasses import dataclass, field

@dataclass #only data, no behaviour state.
class Document:
    title: str
    text: str
    tags: list[str] = field(default_factory=list)   # mutable default, done safely
    score: float = 0.0

doc = Document("RAG basics", "Retrieval augmented generation...", ["rag"])
print(doc)                  # Document(title='RAG basics', text=..., tags=['rag'], score=0.0)
print(doc.title)            # attribute access with a dot, not ["title"]
doc.score = 0.9