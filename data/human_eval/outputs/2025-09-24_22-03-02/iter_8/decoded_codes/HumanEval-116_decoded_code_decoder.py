from typing import List

def number_of_ones_in_binary_representation(x: int) -> int:
    binary_string = bin(x)[2:]
    count_ones = binary_string.count('1')
    return count_ones

def sort_array(arr: List[int]) -> List[int]:
    return sorted(sorted(arr), key=number_of_ones_in_binary_representation)