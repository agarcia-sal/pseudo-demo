from typing import List


def smallest_change(array_of_integers: List[int]) -> int:
    def helper(current_pos: int) -> int:
        if current_pos >= len(array_of_integers) / 2:
            return 0
        if array_of_integers[current_pos] != array_of_integers[len(array_of_integers) - current_pos - 1]:
            return 1 + helper(current_pos + 1)
        else:
            return helper(current_pos + 1)

    return helper(0)