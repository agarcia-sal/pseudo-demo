from typing import List

class Solution:
    def occurrencesOfElement(self, nums: List[int], queries: List[int], x: int) -> List[int]:
        positions = []
        idx = 0
        while idx < len(nums):
            current = nums[idx]
            if not (current != x):
                positions.append(idx)
            idx += 1

        results = []
        qidx = 0
        while qidx < len(queries):
            q = queries[qidx]
            if q <= len(positions):
                posIndex = q - 1
                val = positions[posIndex]
                results.append(val)
            else:
                results.append(-1)
            qidx += 1

        return results