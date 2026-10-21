nums = [10, 20, 30, 40, 50, 60]

nums[1:4]     # [20, 30, 40]   (start included, end excluded)
nums[:3]      # [10, 20, 30]   first 3
nums[3:]      # [40, 50, 60]   from index 3 onward
nums[::2]     # [10, 30, 50]   every 2nd item

# Batching, e.g. sending 2 docs at a time to an API
batch_size = 2
for i in range(0, len(nums), batch_size):
    batch = nums[i:i + batch_size]
    print(batch)


words = ["rag", "agent", "llm"]

upper = [w.upper() for w in words]               # ['RAG', 'AGENT', 'LLM']
long_words = [w for w in words if len(w) > 3]    # ['agent']
lengths = [len(w) for w in words]     


sorted([3, 1, 2])                     # [1, 2, 3] (returns a new list)
sorted(words, key=len)                # sort by length
sum([1, 2, 3]); max([1, 2, 3])
", ".join(words)                      # "rag, agent, llm"

a = [1, 2]
b = a              # NOT a copy: both names point to the same list
b = a.copy()       # real copy (or a[:])           # [3, 5, 3]


