from typing import List, Optional

def next_smallest(input_array: List[int]) -> Optional[int]:
    filtered_array = list(set(input_array))
    sorted_array = sorted(filtered_array)
    if len(sorted_array) < 2:
        return None
    else:
        return sorted_array[1]