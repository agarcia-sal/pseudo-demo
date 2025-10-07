from typing import List, Optional, Tuple


def find_closest_elements(list_of_numbers: List[float]) -> Optional[Tuple[float, float]]:
    best_match: Optional[Tuple[float, float]] = None
    minimal_gap: Optional[float] = None

    n = len(list_of_numbers)
    for i in range(n):
        first_val = list_of_numbers[i]
        for j in range(n):
            if i == j:
                continue
            second_val = list_of_numbers[j]

            current_gap = first_val - second_val
            if minimal_gap is None:
                minimal_gap = abs(current_gap)
                best_match = (first_val, second_val) if first_val < second_val else (second_val, first_val)
            else:
                alternative_gap = second_val - first_val
                absolute_gap = abs(alternative_gap)
                if absolute_gap < minimal_gap:
                    minimal_gap = absolute_gap
                    best_match = (first_val, second_val) if first_val < second_val else (second_val, first_val)

    return best_match