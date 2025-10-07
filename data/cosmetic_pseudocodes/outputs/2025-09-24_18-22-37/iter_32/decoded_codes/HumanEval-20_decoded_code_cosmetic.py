from typing import List, Optional, Tuple

def find_closest_elements(list_of_numbers: List[int]) -> Optional[Tuple[int, int]]:
    candidate_pair: Optional[Tuple[int, int]] = None
    smallest_gap: Optional[int] = None

    outer_pos = 0
    while outer_pos < len(list_of_numbers):
        first_val = list_of_numbers[outer_pos]
        inner_pos = 0
        while inner_pos < len(list_of_numbers):
            if outer_pos == inner_pos:
                inner_pos += 1
                continue

            second_val = list_of_numbers[inner_pos]
            if smallest_gap is None:
                diff_abs = abs(first_val - second_val)
                smallest_gap = diff_abs
                if first_val < second_val:
                    candidate_pair = (first_val, second_val)
                else:
                    candidate_pair = (second_val, first_val)
            else:
                current_gap = abs(first_val - second_val)
                if current_gap < smallest_gap:
                    smallest_gap = current_gap
                    if second_val < first_val:
                        candidate_pair = (second_val, first_val)
                    else:
                        candidate_pair = (first_val, second_val)

            inner_pos += 1
        outer_pos += 1

    return candidate_pair