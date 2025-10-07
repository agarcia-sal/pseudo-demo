from typing import List

class Solution:
    def canSortArray(self, nums: List[int]) -> bool:
        def count_set_bits(n: int) -> int:
            return bin(n).count('1')

        n = len(nums)
        sorted_nums = sorted(nums)

        for _ in range(n):
            for j in range(n - 1):
                if count_set_bits(nums[j]) == count_set_bits(nums[j + 1]) and nums[j] > nums[j + 1]:
                    nums[j], nums[j + 1] = nums[j + 1], nums[j]

        return nums == sorted_nums