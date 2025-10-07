from typing import List

def pairs_sum_to_zero(array_of_ints: List[int]) -> bool:
    def helper(current_pos: int, array_len: int) -> bool:
        if current_pos >= array_len:
            return False

        def inner_loop(inner_idx: int) -> bool:
            if inner_idx >= array_len:
                return False
            if array_of_ints[current_pos] + array_of_ints[inner_idx] == 0:
                return True
            return inner_loop(inner_idx + 1)

        if inner_loop(current_pos + 1):
            return True
        return helper(current_pos + 1, array_len)

    return helper(0, len(array_of_ints))