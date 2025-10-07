from typing import List, Optional

def rolling_max(list_of_numbers: List[int]) -> List[int]:
    current_peak: Optional[int] = None
    accumulative_results: List[int] = []

    for current_value in list_of_numbers:
        if current_peak is None or current_value > current_peak:
            current_peak = current_value
        accumulative_results.append(current_peak)

    return accumulative_results