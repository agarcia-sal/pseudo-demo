from typing import List, Optional

def rolling_max(list_of_numbers: List[int]) -> List[int]:
    current_peak: Optional[int] = None
    accumulation: List[int] = []
    iterator_position: int = 0

    while iterator_position < len(list_of_numbers):
        candidate = list_of_numbers[iterator_position]

        if current_peak is not None:
            if candidate > current_peak:
                current_peak = candidate
        else:
            current_peak = candidate

        accumulation.append(current_peak)
        iterator_position += 1

    return accumulation