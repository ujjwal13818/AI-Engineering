def stats(nums):
    return min(nums), max(nums), sum(nums) / len(nums)

lo, hi, avg = stats([5, 2, 9])
print(lo, hi, avg)

terms = ["rag", "llm", "rag", "agent", "llm", "embedding"]
unique_terms = set(terms)
print(unique_terms)
print(len(terms) - len(unique_terms))

stopwords = {"the", "a", "is", "of"}
sentence = "the cost of a model is high"
words = [w for w in sentence.split() if w not in stopwords]
print(words)

print(set(sentence.split()) - stopwords)  # This will work correctly

skills_needed = {"python", "sql", "docker", "rag"}
skills_have = {"python", "sql"}
print(skills_needed - skills_have)