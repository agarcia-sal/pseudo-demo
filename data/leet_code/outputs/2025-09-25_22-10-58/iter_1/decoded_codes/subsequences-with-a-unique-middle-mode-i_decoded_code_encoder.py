from collections import Counter
from itertools import combinations

class Solution:
    def subsequencesWithMiddleMode(self, nums):
        MOD = 10**9 + 7
        n = len(nums)
        if n < 5:
            return 0
        count = 0
        for subseq in combinations(nums, 5):
            freq = Counter(subseq)
            middle_element = subseq[2]
            middle_count = freq[middle_element]
            is_unique_mode = True
            for num, cnt in freq.items():
                if num != middle_element and cnt >= middle_count:
                    is_unique_mode = False
                    break
            if is_unique_mode:
                count += 1
        return count % MOD