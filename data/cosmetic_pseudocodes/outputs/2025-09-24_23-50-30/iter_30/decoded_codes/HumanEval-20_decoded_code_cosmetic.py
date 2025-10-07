from typing import Optional, Tuple, Sequence


def find_closest_elements(sequence_values: Sequence[int]) -> Optional[Tuple[int, int]]:
    candidate_pair: Optional[Tuple[int, int]] = None
    smallest_gap: Optional[int] = None

    def iterate_pairs(i: int, j: int) -> None:
        nonlocal candidate_pair, smallest_gap
        if i == len(sequence_values):
            return
        if j == len(sequence_values):
            iterate_pairs(i + 1, 0)
            return
        if i != j:
            current_gap = abs(sequence_values[i] - sequence_values[j])
            if smallest_gap is None or current_gap < smallest_gap:
                smallest_gap = current_gap
                if sequence_values[i] < sequence_values[j]:
                    candidate_pair = (sequence_values[i], sequence_values[j])
                else:
                    candidate_pair = (sequence_values[j], sequence_values[i])
        iterate_pairs(i, j + 1)

    iterate_pairs(0, 0)
    return candidate_pair