from typing import List

def sort_array(array: List[int]) -> List[int]:
    array_sorted_by_value: List[int] = sorted(array)
    return sorted(array_sorted_by_value, key=lambda x: bin(x).count('1'))