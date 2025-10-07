from typing import List, Optional, Tuple

def find_closest_elements(numbers_list: List[int]) -> Optional[Tuple[int, int]]:
    pair_closest: Optional[Tuple[int, int]] = None
    dist_minimum: Optional[int] = None
    pos_outer: int = 0

    while pos_outer < len(numbers_list):
        value_outer: int = numbers_list[pos_outer]
        pos_inner: int = 0

        while pos_inner < len(numbers_list):
            value_inner: int = numbers_list[pos_inner]

            if pos_outer != pos_inner:
                dist_current: int = abs(value_outer - value_inner)
                if dist_minimum is None:
                    dist_minimum = dist_current
                    if value_outer <= value_inner:
                        pair_closest = (value_outer, value_inner)
                    else:
                        pair_closest = (value_inner, value_outer)
                else:
                    if dist_current < dist_minimum:
                        dist_minimum = dist_current
                        if value_outer <= value_inner:
                            pair_closest = (value_outer, value_inner)
                        else:
                            pair_closest = (value_inner, value_outer)
                # after processing difference for this pair, break the switch equivalent (continue inner loop)
                # but here no need to do anything, just proceed to next inner iteration
            pos_inner += 1
        pos_outer += 1

    return pair_closest