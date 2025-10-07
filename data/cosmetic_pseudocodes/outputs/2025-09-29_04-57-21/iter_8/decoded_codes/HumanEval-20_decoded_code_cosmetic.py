from typing import List, Optional, Tuple


def find_closest_elements(list_of_numbers: List[int]) -> Optional[Tuple[int, int]]:
    best_match: Optional[Tuple[int, int]] = None
    smallest_gap: Optional[int] = None

    outer_idx = 0
    while outer_idx < len(list_of_numbers) - 1:
        current_num = list_of_numbers[outer_idx]

        inner_idx = 0
        while inner_idx < len(list_of_numbers) - 1:
            comparison_num = list_of_numbers[inner_idx]

            if outer_idx != inner_idx:
                gap_candidate = abs(comparison_num - current_num)
                if smallest_gap is None or gap_candidate < smallest_gap:
                    smallest_gap = gap_candidate
                    best_match = (min(comparison_num, current_num), max(comparison_num, current_num))

            inner_idx += 1
        outer_idx += 1

    return best_match