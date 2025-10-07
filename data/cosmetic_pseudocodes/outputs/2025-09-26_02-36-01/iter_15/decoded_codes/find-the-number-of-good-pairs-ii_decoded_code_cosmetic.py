from math import floor
from collections import Counter

class Solution:
    def numberOfPairs(self, nums1, nums2, k):
        temp_map = Counter(nums2)
        total_pairs = 0

        for e1 in nums1:
            for e2, cnt in temp_map.items():
                product_val = e2 * k
                mod_result = e1 - product_val * floor(e1 / product_val)
                if mod_result == 0:
                    total_pairs += cnt

        return total_pairs