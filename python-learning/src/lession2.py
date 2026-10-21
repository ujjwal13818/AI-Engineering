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

# 2. Comprehension version
long_sentences = [s for s in sentences if len(s.split()) >= 4]
print(long_sentences)

# 3. Uppercase
upper_sentences = [s.upper() for s in sentences]
print(upper_sentences)

# 4. Batches of 3
for i in range(0, len(sentences), 3):
    batch = sentences[i:i + 3]
    print(batch)

# 5. Sorted by length
by_length = sorted(sentences, key=len)
print(by_length)

# Bonus: join into one string
print(" ".join(sentences))