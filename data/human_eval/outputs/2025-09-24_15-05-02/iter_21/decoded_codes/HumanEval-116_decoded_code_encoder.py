from typing import List

def sort_array(array: List[int]) -> List[int]:
    sorted_by_value = sorted(array)
    sorted_by_ones = sorted(sorted_by_value, key=lambda x: bin(x).count('1'))
    return sorted_by_ones