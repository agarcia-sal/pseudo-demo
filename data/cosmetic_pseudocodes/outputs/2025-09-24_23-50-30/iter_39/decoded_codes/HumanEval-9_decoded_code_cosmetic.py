from typing import List, Optional

def rolling_max(array_elements: List[int]) -> List[int]:
    def helper(current_index: int, current_peak: Optional[int], acc: List[int]) -> List[int]:
        if current_index == len(array_elements):
            return acc
        element = array_elements[current_index]
        updated_peak = element if current_peak is None or element > current_peak else current_peak
        return helper(current_index + 1, updated_peak, acc + [updated_peak])
    return helper(0, None, [])