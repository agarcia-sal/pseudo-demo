from typing import List, Optional, Tuple


def find_closest_elements(list_of_numbers: List[int]) -> Optional[Tuple[int, int]]:
    pair_closest: Optional[Tuple[int, int]] = None
    min_diff: Optional[int] = None

    def explore(i: int, j: int) -> None:
        nonlocal pair_closest, min_diff
        if j == len(list_of_numbers):
            return
        if i == len(list_of_numbers):
            explore(0, j + 1)
            return
        if i != j:
            diff_current = abs(list_of_numbers[i] - list_of_numbers[j])
            if min_diff is None or diff_current < min_diff:
                min_diff = diff_current
                pair_closest = (
                    min(list_of_numbers[i], list_of_numbers[j]),
                    max(list_of_numbers[i], list_of_numbers[j]),
                )
        explore(i + 1, j)

    explore(0, 0)
    return pair_closest