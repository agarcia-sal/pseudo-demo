from typing import List

def sort_array(array: List[int]) -> List[int]:
    # First, sort ascending by decimal value to ensure stability for the next sort
    array_sorted_by_value = sorted(array)
    # Then sort ascending by count of ones in binary representation
    sorted_array = sorted(array_sorted_by_value, key=lambda x: bin(x).count('1'))
    return sorted_array