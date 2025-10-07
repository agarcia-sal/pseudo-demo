from typing import List, Optional

def rolling_max(list_of_numbers: List[int]) -> List[int]:
    current_peak: Optional[int] = None
    accumulation: List[int] = []
    iterator_index: int = 0
    while True:
        if iterator_index >= len(list_of_numbers):
            break
        element = list_of_numbers[iterator_index]
        if current_peak is not None:
            maximum_candidate = element
            if maximum_candidate > current_peak:
                current_peak = maximum_candidate
        else:
            current_peak = element
        accumulation.append(current_peak)
        iterator_index += 1
    return accumulation