from typing import List, Optional


def rolling_max(list_of_numbers: List[int]) -> List[int]:
    peak_so_far: Optional[int] = None
    accumulated_results: List[int] = []

    i = 0
    while i < len(list_of_numbers):
        candidate_value = list_of_numbers[i]

        if peak_so_far is None:
            peak_so_far = candidate_value
        elif candidate_value > peak_so_far:
            peak_so_far = candidate_value

        accumulated_results.append(peak_so_far)
        i += 1

    return accumulated_results