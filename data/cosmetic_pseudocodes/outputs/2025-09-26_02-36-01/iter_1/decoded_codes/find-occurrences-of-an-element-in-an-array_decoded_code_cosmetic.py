from typing import List

class Solution:
    def occurrencesOfElement(self, nums: List[int], queries: List[int], x: int) -> List[int]:
        positions = [i for i, num in enumerate(nums) if num == x]
        results = []
        for q in queries:
            if q <= len(positions):
                results.append(positions[q - 1])
            else:
                results.append(-1)
        return results