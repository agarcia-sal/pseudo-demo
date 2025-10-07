from typing import List

def pairs_sum_to_zero(array_of_nums: List[int]) -> bool:
    def check_indices(pos_left: int, pos_right: int) -> bool:
        if pos_left >= len(array_of_nums) - 1:
            return False
        if pos_right >= len(array_of_nums):
            return check_indices(pos_left + 1, pos_left + 2)

        val_one = array_of_nums[pos_left]
        val_two = array_of_nums[pos_right]

        if val_one + val_two == 0:
            return True
        return check_indices(pos_left, pos_right + 1)

    return check_indices(0, 1)