from typing import List


def has_close_elements(arr_nums: List[int], limit_val: int) -> bool:
    def check_pairs(i_outer: int) -> bool:
        if i_outer >= len(arr_nums):
            return False

        def check_inner(i_inner: int) -> bool:
            if i_inner >= len(arr_nums):
                return check_pairs(i_outer + 1)

            if i_inner != i_outer:
                diff_abs = abs(arr_nums[i_inner] - arr_nums[i_outer])
                if diff_abs < limit_val:
                    return True

            return check_inner(i_inner + 1)

        return check_inner(0)

    return check_pairs(0)