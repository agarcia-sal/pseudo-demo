from typing import Sequence, Optional, Tuple


def find_closest_elements(input_sequence: Sequence[int]) -> Optional[Tuple[int, int]]:
    def recursive_scan(
        primary_idx: int,
        candidate_idx: int,
        current_best: Optional[Tuple[int, int]],
        current_least: Optional[int],
    ) -> Optional[Tuple[int, int]]:
        if primary_idx >= len(input_sequence):
            return current_best
        if candidate_idx >= len(input_sequence):
            return recursive_scan(primary_idx + 1, 0, current_best, current_least)

        a_val = input_sequence[primary_idx]
        b_val = input_sequence[candidate_idx]

        if primary_idx != candidate_idx:
            diff_val = abs(a_val - b_val)
            update_needed = current_least is None or diff_val < current_least
            if update_needed:
                new_best = tuple(sorted((a_val, b_val)))
                new_least = diff_val
                return recursive_scan(primary_idx, candidate_idx + 1, new_best, new_least)
            else:
                return recursive_scan(primary_idx, candidate_idx + 1, current_best, current_least)
        else:
            return recursive_scan(primary_idx, candidate_idx + 1, current_best, current_least)

    return recursive_scan(0, 0, None, None)