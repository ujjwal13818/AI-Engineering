from dataclasses import dataclass, field

@dataclass #no need to write __init__, __repr__, __eq__, etc.
class Message:
    role: str
    content: str

    def to_dict(self) -> dict[str, str]:
        return {"role": self.role, "content": self.content}

class Conversation:
    def __init__(self, system_prompt: str) -> None:
        self.messages: list[Message] = [Message("System", system_prompt)]

    def add(self, role: str, content: str) -> None:
        self.messages.append(Message(role, content))

    def to_api_format(self) -> list[dict[str, str]]:
        return [msg.to_dict() for msg in self.messages]


convo = Conversation("You are a helpful assistant.")
convo.add("user", "What is RAG?")
convo.add("assistant", "RAG is Retrieval-Augmented Generation.")
print(convo.to_api_format())