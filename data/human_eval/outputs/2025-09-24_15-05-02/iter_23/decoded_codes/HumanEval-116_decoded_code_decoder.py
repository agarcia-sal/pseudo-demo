from typing import List

def sort_array(array: List[int]) -> List[int]:
    # Sort array in ascending order by value first
    array_sorted_by_value = sorted(array)
    # Then stable sort by the count of '1's in the binary representation
    array_sorted_by_value.sort(key=lambda x: bin(x).count('1'))
    return array_sorted_by_value