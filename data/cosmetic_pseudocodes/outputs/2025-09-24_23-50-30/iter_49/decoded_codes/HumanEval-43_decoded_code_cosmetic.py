from typing import List


def pairs_sum_to_zero(array_of_numbers: List[int]) -> bool:
    def check_pairs_recursive(current_idx: int, next_idx: int) -> bool:
        if current_idx >= len(array_of_numbers) - 1:
            return False
        elif next_idx >= len(array_of_numbers):
            return check_pairs_recursive(current_idx + 1, current_idx + 2)
        else:
            if array_of_numbers[current_idx] + array_of_numbers[next_idx] == 0:
                return True
            else:
                return check_pairs_recursive(current_idx, next_idx + 1)

    return check_pairs_recursive(0, 1)