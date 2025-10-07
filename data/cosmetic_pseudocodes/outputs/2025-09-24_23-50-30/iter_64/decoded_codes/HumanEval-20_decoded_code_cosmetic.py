from typing import Sequence, Optional, Tuple

def find_closest_elements(p_sequence: Sequence[int]) -> Optional[Tuple[int, int]]:
    a_min_distance: Optional[int] = None
    a_best_pair: Optional[Tuple[int, int]] = None

    def iterate_outer(o_idx: int) -> None:
        if o_idx >= len(p_sequence):
            return
        def iterate_inner(i_idx: int) -> None:
            if i_idx >= len(p_sequence):
                return
            if o_idx != i_idx:
                d_val = abs(p_sequence[o_idx] - p_sequence[i_idx])
                nonlocal a_min_distance, a_best_pair
                if a_min_distance is None or d_val < a_min_distance:
                    a_min_distance = d_val
                    a_best_pair = tuple(sorted((p_sequence[o_idx], p_sequence[i_idx])))
            iterate_inner(i_idx + 1)
        iterate_inner(0)
        iterate_outer(o_idx + 1)

    iterate_outer(0)
    return a_best_pair