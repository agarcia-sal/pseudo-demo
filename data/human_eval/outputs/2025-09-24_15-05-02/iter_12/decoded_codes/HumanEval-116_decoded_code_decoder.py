from typing import List

def sort_array(array: List[int]) -> List[int]:
    array_sorted_by_value = sorted(array)
    array_sorted = sorted(array_sorted_by_value, key=lambda x: bin(x).count('1'))
    return array_sorted