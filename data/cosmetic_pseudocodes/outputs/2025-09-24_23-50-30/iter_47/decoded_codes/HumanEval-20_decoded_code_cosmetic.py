from typing import List, Optional, Tuple


def find_closest_elements(input_list: List[int]) -> Optional[Tuple[int, int]]:
    pair_result: Optional[Tuple[int, int]] = None
    smallest_gap: Optional[int] = None
    pos_a: int = 0

    while pos_a < len(input_list):
        val_a = input_list[pos_a]
        pos_b = 0

        while pos_b < len(input_list):
            val_b = input_list[pos_b]

            if pos_a != pos_b:
                if smallest_gap is None:
                    gap = val_a - val_b
                    if gap < 0:
                        gap = -gap
                    smallest_gap = gap
                    if val_a < val_b:
                        pair_result = (val_a, val_b)
                    else:
                        pair_result = (val_b, val_a)
                else:
                    distance_candidate = val_a + (-val_b)
                    if distance_candidate < 0:
                        distance_candidate = -distance_candidate

                    if distance_candidate < smallest_gap:
                        smallest_gap = distance_candidate
                        if val_a < val_b:
                            pair_result = (val_a, val_b)
                        else:
                            pair_result = (val_b, val_a)
            pos_b += 1
        pos_a += 1

    return pair_result