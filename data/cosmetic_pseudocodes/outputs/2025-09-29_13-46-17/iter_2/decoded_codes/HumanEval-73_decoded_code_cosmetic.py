from typing import List

def smallest_change(array_of_integers: List[int]) -> int:
    def count_differences(current_idx: int, limit_idx: int, tally: int) -> int:
        if current_idx == limit_idx:
            return tally
        left_val = array_of_integers[current_idx]
        right_val = array_of_integers[len(array_of_integers) - 1 - current_idx]
        new_tally = tally + (left_val != right_val)
        return count_differences(current_idx + 1, limit_idx, new_tally)
    return count_differences(0, len(array_of_integers) // 2, 0)