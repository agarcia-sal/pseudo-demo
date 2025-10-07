from typing import List

class Solution:
    def occurrencesOfElement(self, nums: List[int], queries: List[int], x: int) -> List[int]:
        positions = []
        idx = 0
        while idx < len(nums):
            currentValue = nums[idx]
            if currentValue == x:
                positions.append(idx)
            idx += 1

        results = []
        qIndex = 0
        while qIndex < len(queries):
            target = queries[qIndex]
            if target <= len(positions):
                resultIndex = target - 1
                results.append(positions[resultIndex])
            else:
                results.append(-1)
            qIndex += 1

        return results