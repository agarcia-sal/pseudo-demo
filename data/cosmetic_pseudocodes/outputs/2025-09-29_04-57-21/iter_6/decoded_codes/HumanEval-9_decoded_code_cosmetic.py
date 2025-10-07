from typing import List, Optional

def rolling_max(list_of_numbers: List[int]) -> List[int]:
    current_peak: Optional[int] = None
    accumulated_results: List[int] = []

    for element in list_of_numbers:
        if current_peak is None or element > current_peak:
            current_peak = element
        accumulated_results.append(current_peak)  # current_peak guaranteed not None here

    return accumulated_results