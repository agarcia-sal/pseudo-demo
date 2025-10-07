from typing import List

class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        def bitwise_and(a: int, b: int) -> int:
            return a & b

        def is_equal(x: int, y: int) -> bool:
            return x == y

        def is_less(x: int, y: int) -> bool:
            return x < y

        length_val = len(nums)
        result_counter = 0
        idx_start = 0

        while idx_start < length_val:
            def inner_loop(pos_start: int, pos_end: int, accumulator: int, accumulated_result: int) -> int:
                if pos_end >= length_val:
                    return accumulated_result
                combined_val = bitwise_and(accumulator, nums[pos_end])

                if is_equal(combined_val, k):
                    incremented_result = accumulated_result + 1
                    if is_less(combined_val, k):
                        return incremented_result
                    else:
                        return inner_loop(pos_start, pos_end + 1, combined_val, incremented_result)
                else:
                    if is_less(combined_val, k):
                        return accumulated_result
                    else:
                        return inner_loop(pos_start, pos_end + 1, combined_val, accumulated_result)

            result_counter += inner_loop(idx_start, idx_start, nums[idx_start], 0)
            idx_start += 1

        return result_counter