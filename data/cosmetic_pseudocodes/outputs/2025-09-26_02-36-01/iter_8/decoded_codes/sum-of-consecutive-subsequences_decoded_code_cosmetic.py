from collections import Counter
from typing import List

class Solution:
    def getSum(self, nums: List[int]) -> int:
        def calc(nums: List[int]) -> int:
            len_nums = len(nums)
            cnt_obj_a = Counter()
            cnt_obj_b = Counter()
            left_counts = [0] * len_nums
            right_counts = [0] * len_nums

            idx = 1
            while idx < len_nums:
                key_a = nums[idx - 1]
                prev_count = cnt_obj_a.get(key_a, 0)
                cnt_obj_a[key_a] = prev_count + 1
                left_counts[idx] = cnt_obj_a[key_a]
                idx += 1

            idx = len_nums - 2
            while idx >= 0:
                key_b = nums[idx + 1]
                prev_count_b = cnt_obj_b.get(key_b, 0)
                cnt_obj_b[key_b] = prev_count_b + 1
                right_counts[idx] = cnt_obj_b[key_b]
                idx -= 1

            sum_accumulator = 0
            pos_ptr = 0
            while pos_ptr < len_nums:
                a_val = left_counts[pos_ptr]
                b_val = right_counts[pos_ptr]
                c_val = nums[pos_ptr]
                part1 = a_val + b_val
                part2 = a_val * b_val
                combined = part1 + part2
                increment = combined * c_val
                sum_accumulator += increment
                pos_ptr += 1

            return sum_accumulator % (10**9 + 7)

        modulus = 10**9 + 7
        val_x = calc(nums)

        reversed_nums = []
        end_ptr = len(nums) - 1
        while end_ptr >= 0:
            reversed_nums.append(nums[end_ptr])
            end_ptr -= 1

        val_y = calc(reversed_nums)

        sum_of_nums = 0
        add_idx = 0
        while add_idx < len(nums):
            sum_of_nums += nums[add_idx]
            add_idx += 1

        return (val_x + val_y + sum_of_nums) % modulus