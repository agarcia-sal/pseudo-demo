from typing import List, Optional, Tuple


def find_closest_elements(list_of_numbers: List[int]) -> Optional[Tuple[int, int]]:
    pair_closest: Optional[Tuple[int, int]] = None
    dist_minimum: Optional[int] = None
    pos_outer: int = 0
    n: int = len(list_of_numbers)

    while pos_outer < n:
        val_outer: int = list_of_numbers[pos_outer]
        pos_inner: int = 0

        while pos_inner < n:
            if pos_inner == pos_outer:
                pos_inner += 1
                continue

            val_inner: int = list_of_numbers[pos_inner]
            dist_current: int = val_outer - val_inner if val_outer > val_inner else val_inner - val_outer

            if dist_minimum is None or dist_current < dist_minimum:
                dist_minimum = dist_current
                pair_candidate = [val_outer, val_inner]
                if pair_candidate[0] > pair_candidate[1]:
                    pair_candidate[0], pair_candidate[1] = pair_candidate[1], pair_candidate[0]
                pair_closest = tuple(pair_candidate)

            pos_inner += 1

        pos_outer += 1

    return pair_closest