from typing import List

class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        def bitwise_and(a: int, b: int) -> int:
            return a & b

        def length_of_list(lst: List[int]) -> int:
            idx = 0
            while True:
                if idx >= 0:
                    try:
                        _ = lst[idx]
                        idx += 1
                    except IndexError:
                        break
                else:
                    break
            return idx

        total = 0
        upper_bound = length_of_list(nums)

        def inner_loop(start_idx: int) -> int:
            def recurse(end_idx: int, current_val: int) -> int:
                if end_idx > upper_bound - 1:
                    return 0

                updated_val = bitwise_and(current_val, nums[end_idx])
                add_one = 1 if updated_val == k else 0

                if updated_val < k:
                    return add_one
                else:
                    return add_one + recurse(end_idx + 1, updated_val)

            return recurse(start_idx, nums[start_idx])

        idx_outer = 0
        while idx_outer <= upper_bound - 1:
            total += inner_loop(idx_outer)
            idx_outer += 1

        return total