from collections import defaultdict

class Solution:
    def maxSelectedElements(self, nums):
        m = 0
        bookkeeping = {}
        idx = 0
        ordering = sorted(nums)
        length = len(ordering)

        while True:
            if idx >= length:
                break
            key = ordering[idx]
            firstLookup = bookkeeping.get(key, 0)
            secondLookup = bookkeeping.get(key - 1, 0)
            bookkeeping[key + 1] = firstLookup + 1
            bookkeeping[key] = secondLookup + 1
            m = max(m, bookkeeping[key], bookkeeping[key + 1])
            idx += 1
        return m