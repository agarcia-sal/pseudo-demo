from typing import List

def maximum(list_of_numbers: List[int], count: int) -> List[int]:
    if count == 0:
        return []
    sorted_numbers = sorted(list_of_numbers)
    return sorted_numbers[-count:]