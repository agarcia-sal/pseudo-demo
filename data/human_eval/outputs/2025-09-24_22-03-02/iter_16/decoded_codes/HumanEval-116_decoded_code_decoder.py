from typing import List

def sort_array(arr: List[int]) -> List[int]:
    sorted_by_value = sorted(arr)
    def key(x: int) -> int:
        binary_representation = bin(x)
        binary_string = binary_representation[2:]
        count_ones = binary_string.count('1')
        return count_ones
    sorted_by_ones = sorted(sorted_by_value, key=key)
    return sorted_by_ones