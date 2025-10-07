from typing import List, Optional

def rolling_max(list_of_numbers: List[int]) -> List[int]:
    current_peak: Optional[int] = None
    accumulated_results: List[int] = []

    idx: int = 0
    while idx < len(list_of_numbers):
        element: int = list_of_numbers[idx]

        if current_peak is None:
            current_peak = element
        else:
            if current_peak < element:
                current_peak = element

        accumulated_results.append(current_peak)
        idx += 1

    return accumulated_results