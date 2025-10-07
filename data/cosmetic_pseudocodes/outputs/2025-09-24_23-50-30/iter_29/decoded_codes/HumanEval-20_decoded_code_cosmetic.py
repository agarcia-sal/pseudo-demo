from typing import Sequence, Optional, Tuple


def find_closest_elements(input_sequence: Sequence[int]) -> Optional[Tuple[int, int]]:
    best_pair: Optional[Tuple[int, int]] = None
    smallest_gap: Optional[int] = None

    pos_outer = 0
    length = len(input_sequence)
    while pos_outer < length:
        pos_inner = 0
        while pos_inner < length:
            if pos_outer != pos_inner:
                diff = abs(input_sequence[pos_outer] - input_sequence[pos_inner])
                if smallest_gap is None or diff < smallest_gap:
                    smallest_gap = diff
                    best_pair = tuple(sorted((input_sequence[pos_outer], input_sequence[pos_inner])))
            pos_inner += 1
        pos_outer += 1

    return best_pair