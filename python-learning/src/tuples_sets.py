point = (3, 4)
x, y = point                 # unpacking, very common

def min_max(nums):
    return min(nums), max(nums)    # returns a tuple

lo, hi = min_max([5, 2, 9])        # lo=2, hi=9

//point[0] = 10                      # TypeError: can't modify


tags = {"ai", "ml", "ai", "nlp"}     # {'ai', 'ml', 'nlp'} duplicates removed
tags.add("rag")
"ml" in tags                         # fast membership check

unique = set(["a", "b", "a"])        # dedupe a list
list(unique)                         # back to a list

a = {"python", "java", "sql"}
b = {"python", "rust"}
a & b      # {'python'}                           intersection
a | b      # {'python','java','sql','rust'}       union
a - b      # {'java', 'sql'}                      difference