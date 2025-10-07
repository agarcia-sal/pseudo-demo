from typing import List, Optional

def rolling_max(list_of_numbers: List[int]) -> List[int]:
    accumulator: List[int] = []
    current_peak: Optional[int] = None
    index: int = 0

    while index < len(list_of_numbers):
        element: int = list_of_numbers[index]

        if current_peak is None:
            current_peak = element
        else:
            if element > current_peak:
                current_peak = element
            # else keep current_peak unchanged

        accumulator.append(current_peak)
        index += 1

    return accumulator