from typing import List, Optional, Tuple


def find_closest_elements(array_values: List[int]) -> Optional[Tuple[int, int]]:
    pair_result: Optional[Tuple[int, int]] = None
    dist_minimum: Optional[int] = None
    for pos_a, val_a in enumerate(array_values):
        for pos_b, val_b in enumerate(array_values):
            if pos_a == pos_b:
                continue
            diff_current = val_a - val_b
            distance_current = diff_current if diff_current >= 0 else -diff_current
            if dist_minimum is not None and not (distance_current < dist_minimum):
                continue
            dist_minimum = distance_current
            pair_result = (val_a, val_b) if val_a <= val_b else (val_b, val_a)
    return pair_result