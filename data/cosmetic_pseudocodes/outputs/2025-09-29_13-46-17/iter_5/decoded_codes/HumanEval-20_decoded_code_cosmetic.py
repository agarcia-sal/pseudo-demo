from typing import Sequence, Optional, Tuple

def find_closest_elements(primary_sequence: Sequence[int]) -> Optional[Tuple[int, int]]:
    closest_pair_result: Optional[Tuple[int, int]] = None
    minimal_gap: Optional[int] = None

    def inner_loop(i: int, j: int, current_pair: Optional[Tuple[int, int]], current_gap: Optional[int]) -> Tuple[Optional[Tuple[int, int]], Optional[int]]:
        if j == len(primary_sequence):
            return current_pair, current_gap
        else:
            a = primary_sequence[i]
            b = primary_sequence[j]
            updated_pair = current_pair
            updated_gap = current_gap

            if i != j:
                temp_diff = abs(a - b)
                if current_gap is None or temp_diff < current_gap:
                    updated_gap = temp_diff
                    updated_pair = (a, b) if a < b else (b, a)

            return inner_loop(i, j + 1, updated_pair, updated_gap)

    def outer_loop(m: int) -> Optional[Tuple[int, int]]:
        nonlocal closest_pair_result, minimal_gap
        if m == len(primary_sequence):
            return closest_pair_result
        else:
            new_pair, new_gap = inner_loop(m, 0, closest_pair_result, minimal_gap)
            closest_pair_result = new_pair
            minimal_gap = new_gap
            return outer_loop(m + 1)

    return outer_loop(0)