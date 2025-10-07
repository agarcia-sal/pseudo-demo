from typing import List, Optional

def rolling_max(list_of_numbers: List[int]) -> List[int]:
    current_peak: Optional[int] = None
    output_array: List[int] = []

    idx: int = 0
    while idx < len(list_of_numbers):
        current_element: int = list_of_numbers[idx]

        if current_peak is None:
            current_peak = current_element
        elif current_element > current_peak:
            current_peak = current_element

        output_array.append(current_peak)
        idx += 1

    return output_array