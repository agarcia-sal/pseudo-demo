from collections import Counter
from typing import List

class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], k: int) -> int:
        frequency_map = Counter(nums2)
        total_pairs = 0
        for current in nums1:
            for key, freq in frequency_map.items():
                product_term = key * k
                if product_term != 0 and current % product_term == 0:
                    total_pairs += freq
        return total_pairs