docs = ["intro to RAG", "vector databases", "fine-tuning"]

# Access
docs[0]        # "intro to RAG"
docs[-1]       # "fine-tuning" (negative index counts from the end)

# Modify
docs.append("agents")          # add to end
docs.insert(1, "embeddings")   # add at index
docs.remove("fine-tuning")     # remove by value
last = docs.pop()              # remove and return last item
docs[0] = "RAG basics"         # replace

# Info
len(docs)                      # size
see = "agents" in docs               # membership check -> True/False
print(see)

# Loop
for doc in docs:
    print(doc)

for i, doc in enumerate(docs):         # index + value together
    print(i, doc)