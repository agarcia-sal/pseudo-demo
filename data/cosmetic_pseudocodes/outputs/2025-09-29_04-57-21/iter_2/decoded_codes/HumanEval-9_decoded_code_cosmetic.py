from typing import List, Optional


def rolling_max(number_sequence: List[int]) -> List[int]:
    peak_value: Optional[int] = None
    accumulated_maxes: List[int] = []
    pointer: int = 0

    while pointer < len(number_sequence):
        current_element = number_sequence[pointer]
        if peak_value is None:
            peak_value = current_element
        elif current_element > peak_value:
            peak_value = current_element
        accumulated_maxes.append(peak_value)
        pointer += 1

    return accumulated_maxes