from typing import List, Optional


def rolling_max(list_of_numbers: List[int]) -> List[int]:
    accumulator: List[int] = []
    current_peak: Optional[int] = None

    for element in list_of_numbers:
        if current_peak is None or element > current_peak:
            current_peak = element
        accumulator.append(current_peak)

    return accumulator