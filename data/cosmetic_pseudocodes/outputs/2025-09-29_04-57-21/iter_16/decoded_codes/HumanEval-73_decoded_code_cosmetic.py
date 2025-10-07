from typing import List


def smallest_change(array_of_integers: List[int]) -> int:
    mismatch_counter: int = 0
    current_pos: int = 0
    n: int = len(array_of_integers)
    while current_pos < (n / 2):
        if array_of_integers[current_pos] != array_of_integers[n - 1 - current_pos]:
            mismatch_counter += 1
        current_pos += 1
    return mismatch_counter