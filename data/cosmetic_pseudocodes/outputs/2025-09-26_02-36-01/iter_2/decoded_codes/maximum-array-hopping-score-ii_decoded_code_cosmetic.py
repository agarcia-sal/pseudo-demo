from typing import List

class Solution:
    def maxScore(self, nums: List[int]) -> int:
        length = len(nums)
        results = [0] * length
        index = length - 2
        while index >= 0:
            best_value = 0
            inner_index = index + 1
            while inner_index < length:
                gap = inner_index - index
                current_score = gap * nums[inner_index]
                candidate = current_score + results[inner_index]
                if best_value < candidate:
                    best_value = candidate
                inner_index += 1
            results[index] = best_value
            index -= 1
        return results[0]