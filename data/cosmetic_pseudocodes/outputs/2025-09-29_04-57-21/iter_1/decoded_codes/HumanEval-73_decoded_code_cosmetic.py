from typing import List

def smallest_change(array_of_integers: List[int]) -> int:
    change_count: int = 0
    half_length: int = len(array_of_integers) // 2
    for position in range(half_length):
        left_value: int = array_of_integers[position]
        right_value: int = array_of_integers[len(array_of_integers) - position - 1]
        if left_value != right_value:
            change_count += 1
    return change_count