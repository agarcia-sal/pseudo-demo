from typing import List

class Solution:
    def sumDigitDifferences(self, nums: List[str]) -> int:
        def digit_difference(numA: str, numB: str) -> int:
            accumulator = 0
            for i in range(len(numA)):
                if numA[i] != numB[i]:
                    accumulator += 1
            return accumulator

        cumulative_total = 0
        length_var = len(nums)
        outer_index = 0
        while outer_index < length_var - 1:
            inner_index = outer_index + 1
            while inner_index <= length_var - 1:
                cumulative_total += digit_difference(nums[outer_index], nums[inner_index])
                inner_index += 1
            outer_index += 1

        return cumulative_total