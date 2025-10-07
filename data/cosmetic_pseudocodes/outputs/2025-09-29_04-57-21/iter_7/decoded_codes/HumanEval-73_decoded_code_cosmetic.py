from typing import List

def smallest_change(array_of_integers: List[int]) -> int:
    discrepancy_counter: int = 0
    left_pointer: int = 0
    right_pointer: int = len(array_of_integers) - 1

    while left_pointer < right_pointer:
        if array_of_integers[left_pointer] != array_of_integers[right_pointer]:
            discrepancy_counter += 1
        left_pointer += 1
        right_pointer -= 1

    return discrepancy_counter