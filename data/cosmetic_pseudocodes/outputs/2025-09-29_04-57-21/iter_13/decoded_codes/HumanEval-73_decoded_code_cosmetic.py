from typing import List

def smallest_change(array_of_integers: List[int]) -> int:
    difference_count = 0

    def helper(current_position: int) -> None:
        nonlocal difference_count
        if current_position >= len(array_of_integers) // 2:
            return
        if array_of_integers[current_position] != array_of_integers[len(array_of_integers) - 1 - current_position]:
            difference_count += 1
        helper(current_position + 1)

    helper(0)
    return difference_count