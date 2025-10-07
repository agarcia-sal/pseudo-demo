from itertools import combinations
from collections import Counter

class Solution:
    def subsequencesWithMiddleMode(self, nums):
        MOD = 10**9 + 7
        n = len(nums)
        if n < 5:
            return 0

        result = 0
        for subset in combinations(nums, 5):
            freq_map = Counter(subset)
            mid_val = subset[2]
            mid_freq = freq_map[mid_val]

            unique_mode_flag = True
            for key, count_val in freq_map.items():
                if key != mid_val and count_val >= mid_freq:
                    unique_mode_flag = False
                    break

            if unique_mode_flag:
                result += 1

        return result % MOD