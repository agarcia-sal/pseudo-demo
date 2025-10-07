from typing import List, Optional


def rolling_max(list_of_numbers: List[float]) -> List[float]:
    current_peak: Optional[float] = None
    accumulated_maxima: List[float] = []

    for current_element in list_of_numbers:
        if current_peak is None or current_element > current_peak:
            current_peak = current_element
        accumulated_maxima.append(current_peak)  # current_peak guaranteed not None here

    return accumulated_maxima