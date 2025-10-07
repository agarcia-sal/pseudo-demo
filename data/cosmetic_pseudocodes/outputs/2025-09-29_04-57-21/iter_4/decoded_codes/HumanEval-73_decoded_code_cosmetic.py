from typing import List

def smallest_change(array_of_integers: List[int]) -> int:
    mismatch_count = 0
    half_length = len(array_of_integers) // 2
    for current_pos in range(half_length):
        left_val = array_of_integers[current_pos]
        right_val = array_of_integers[len(array_of_integers) - 1 - current_pos]
        if left_val != right_val:
            mismatch_count += 1
    return mismatch_count