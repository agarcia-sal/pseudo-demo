from typing import Sequence, Optional, Tuple

def find_closest_elements(sequence: Sequence[int]) -> Optional[Tuple[int, int]]:
    pair_result: Optional[Tuple[int, int]] = None
    smallest_gap: Optional[int] = None

    length = len(sequence)
    for counter_a in range(length):
        value_a = sequence[counter_a]
        for counter_b in range(length):
            if counter_a != counter_b:
                value_b = sequence[counter_b]
                current_diff = abs(value_a - value_b)
                if smallest_gap is None:
                    smallest_gap = current_diff
                    pair_result = (value_a, value_b) if value_a < value_b else (value_b, value_a)
                elif current_diff < smallest_gap:
                    smallest_gap = current_diff
                    pair_result = (value_a, value_b) if value_a < value_b else (value_b, value_a)

    return pair_result