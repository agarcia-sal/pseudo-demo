from typing import Sequence, Optional, Tuple


def find_closest_elements(sequence_input: Sequence[int]) -> Optional[Tuple[int, int]]:
    candidate_pair: Optional[Tuple[int, int]] = None
    shortest_gap: Optional[int] = None

    for first_idx, first_val in enumerate(sequence_input):
        for second_idx, second_val in enumerate(sequence_input):
            if first_idx != second_idx:
                difference = abs(first_val - second_val)
                if shortest_gap is None or difference < shortest_gap:
                    shortest_gap = difference
                    candidate_pair = tuple(sorted((first_val, second_val)))

    return candidate_pair