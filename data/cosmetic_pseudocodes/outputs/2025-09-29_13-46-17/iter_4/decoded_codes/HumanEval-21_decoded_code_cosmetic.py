from typing import List

def rescale_to_unit(original_array: List[float]) -> List[float]:
    sorted_values = sorted(original_array)
    minimum_found = sorted_values[0]
    difference_found = sorted_values[-1] - minimum_found

    def normalize_element(idx: int) -> List[float]:
        if idx == len(original_array):
            return []
        adjusted = (original_array[idx] - minimum_found) / difference_found
        return [adjusted] + normalize_element(idx + 1)

    return normalize_element(0)