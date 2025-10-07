from typing import List, Optional

def rolling_max(list_of_numbers: List[int]) -> List[int]:
    current_peak: Optional[int] = None
    output_array: List[int] = [0] * len(list_of_numbers)
    index_counter: int = 0

    while index_counter < len(list_of_numbers):
        candidate: int = list_of_numbers[index_counter]
        if current_peak is None:
            current_peak = candidate
        else:
            current_peak = current_peak if current_peak > candidate else candidate
        output_array[index_counter] = current_peak
        index_counter += 1

    return output_array