from collections import Counter
from typing import List

class Solution:
    def getSum(self, nums: List[int]) -> int:
        def calc(nums: List[int]) -> int:
            limit = 10**9 + 7
            length = len(nums)
            left_accumulator = [0] * length
            right_accumulator = [0] * length
            frequency_map = Counter()

            for index in range(1, length):
                prev_elem = nums[index - 1]
                frequency_map[prev_elem] += 1
                left_accumulator[index] = frequency_map[prev_elem]

            frequency_map = Counter()
            for idx_rev in range(length - 2, -1, -1):
                next_elem = nums[idx_rev + 1]
                frequency_map[next_elem] += 1
                right_accumulator[idx_rev] = frequency_map[next_elem]

            accumulator_sum = 0
            for i in range(length):
                l = left_accumulator[i]
                r = right_accumulator[i]
                val = nums[i]
                partial_sum = ((l + r) + (l * r)) * val
                accumulator_sum += partial_sum

            return accumulator_sum % limit

        modulo_val = 10**9 + 7

        res_x = calc(nums)

        reversed_nums = nums[::-1]

        res_y = calc(reversed_nums)

        sum_elements = sum(nums)

        return (res_x + res_y + sum_elements) % modulo_val