from typing import List, Optional

def rolling_max(list_of_numbers: List[int]) -> List[int]:
    accumulator: List[int] = []
    current_peak: Optional[int] = None
    position: int = 0
    length_of_input: int = len(list_of_numbers)

    while position < length_of_input:
        element: int = list_of_numbers[position]

        if current_peak is not None:
            temp_max: int = element if element > current_peak else current_peak
        else:
            temp_max = element

        current_peak = temp_max
        accumulator.append(current_peak)
        position += 1

    return accumulator