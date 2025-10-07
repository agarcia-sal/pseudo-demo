from typing import List

def sort_array(arr: List[int]) -> List[int]:
    # Sort by ascending decimal value first
    arr_sorted_by_value = sorted(arr)
    # Then sort by the count of '1's in the binary representation
    return sorted(arr_sorted_by_value, key=lambda x: bin(x)[2:].count('1'))