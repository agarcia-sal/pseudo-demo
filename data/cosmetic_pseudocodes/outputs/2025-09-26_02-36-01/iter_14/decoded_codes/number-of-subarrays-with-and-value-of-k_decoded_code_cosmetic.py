from typing import List

class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        L = len(nums)
        total = 0

        def helper(index1: int, index2: int, acc_and: int, acc_val: int) -> int:
            if index2 >= L:
                return acc_val
            updated_and = acc_and & nums[index2]
            if updated_and == k:
                return helper(index1, index2 + 1, updated_and, acc_val + 1)
            elif updated_and < k:
                return acc_val
            else:
                return helper(index1, index2 + 1, updated_and, acc_val)

        position = 0
        while position < L:
            total += helper(position, position, nums[position], 0)
            position += 1

        return total