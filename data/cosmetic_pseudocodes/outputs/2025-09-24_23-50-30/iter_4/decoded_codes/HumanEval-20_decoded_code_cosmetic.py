from typing import List, Optional, Tuple


def find_closest_elements(list_of_numbers: List[int]) -> Optional[Tuple[int, int]]:
    closest_pair: Optional[Tuple[int, int]] = None
    minimum_distance: float = float('inf')

    def check_pairs(i: int) -> None:
        nonlocal closest_pair, minimum_distance
        if i >= len(list_of_numbers):
            return

        def inner_check(j: int) -> None:
            nonlocal closest_pair, minimum_distance
            if j >= len(list_of_numbers):
                return

            if i != j:
                diff = abs(list_of_numbers[i] - list_of_numbers[j])
                if diff < minimum_distance:
                    minimum_distance = diff
                    # Sort the pair to keep order consistent
                    pair = (list_of_numbers[i], list_of_numbers[j])
                    closest_pair = tuple(sorted(pair))

            inner_check(j + 1)

        inner_check(0)
        check_pairs(i + 1)

    check_pairs(0)
    return closest_pair