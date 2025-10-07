from typing import Sequence, Optional, Tuple

def find_closest_elements(numbers_collection: Sequence[int]) -> Optional[Tuple[int, int]]:
    closest_pair_result: Optional[Tuple[int, int]] = None
    smallest_diff: Optional[int] = None

    def inner_loop(i_outer: int, i_inner: int) -> None:
        nonlocal closest_pair_result, smallest_diff
        if i_outer >= len(numbers_collection):
            return
        if i_inner >= len(numbers_collection):
            inner_loop(i_outer + 1, 0)
            return
        if i_outer != i_inner:
            difference_value = abs(numbers_collection[i_outer] - numbers_collection[i_inner])
            if smallest_diff is None or difference_value < smallest_diff:
                smallest_diff = difference_value
                a, b = numbers_collection[i_outer], numbers_collection[i_inner]
                if a > b:
                    a, b = b, a
                closest_pair_result = (a, b)
        inner_loop(i_outer, i_inner + 1)

    inner_loop(0, 0)
    return closest_pair_result