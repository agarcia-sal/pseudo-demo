from typing import Sequence, Optional, Tuple


def find_closest_elements(p_sequence: Sequence[int]) -> Optional[Tuple[int, int]]:
    result_pair: Optional[Tuple[int, int]] = None
    least_gap: Optional[int] = None

    length = len(p_sequence)
    for outer in range(length):
        for inner in range(length):
            if outer != inner:
                diff = abs(p_sequence[outer] - p_sequence[inner])
                if least_gap is None or diff < least_gap:
                    least_gap = diff
                    a, b = p_sequence[outer], p_sequence[inner]
                    if a > b:
                        a, b = b, a
                    result_pair = (a, b)

    return result_pair