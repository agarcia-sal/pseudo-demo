from typing import List


def smallest_change(array_of_integers: List[int]) -> int:
    mismatches: int = 0
    midpoint: int = (len(array_of_integers) // 2) - 1

    def check_pair(i: int) -> None:
        nonlocal mismatches
        if i > midpoint:
            return
        if array_of_integers[i] != array_of_integers[len(array_of_integers) - 1 - i]:
            mismatches += 1
        check_pair(i + 1)

    check_pair(0)
    return mismatches