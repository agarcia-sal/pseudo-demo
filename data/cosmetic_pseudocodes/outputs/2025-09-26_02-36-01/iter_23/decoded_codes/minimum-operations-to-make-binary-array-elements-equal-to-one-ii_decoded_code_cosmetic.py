from typing import List

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        count = 0
        toggle = 0

        def traverse(index: int):
            nonlocal count, toggle
            if index < len(nums):
                parity = toggle % 2
                if parity == 0:
                    element = nums[index]
                else:
                    element = 1 - nums[index]
                if element == 0:
                    count += 1
                    toggle += 1
                traverse(index + 1)

        traverse(0)
        return count