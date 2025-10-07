from typing import List

def smallest_change(array_of_integers: List[int]) -> int:
    total_differences: int = 0
    midpoint: int = len(array_of_integers) // 2
    for position in range(midpoint):
        left_val = array_of_integers[position]
        right_val = array_of_integers[len(array_of_integers) - 1 - position]
        total_differences += 1 if left_val != right_val else 0
    return total_differences