from collections import Counter
from typing import List

class Solution:
    def gcdValues(self, nums: List[int], queries: List[int]) -> List[int]:
        occur = Counter(nums)
        peak = max(nums) if nums else 0

        tally = [0] * (peak + 1)
        helper2 = peak

        # Precompute tally using inclusion-exclusion principle over multiples
        while helper2 >= 1:
            delta = 0
            beta = helper2
            while beta <= peak:
                delta += occur.get(beta, 0)
                tally[helper2] -= tally[beta]
                beta += helper2
            helper1 = delta * (delta - 1) // 2
            tally[helper2] += helper1
            helper2 -= 1

        prefix_accumulation = [0]
        for eta in tally:
            prefix_accumulation.append(prefix_accumulation[-1] + eta)

        output_list = []
        for query_element in queries:
            low, high = 0, len(prefix_accumulation) - 1
            while low < high:
                mid = (low + high) // 2
                if prefix_accumulation[mid] <= query_element:
                    low = mid + 1
                else:
                    high = mid
            output_list.append(low)

        return output_list