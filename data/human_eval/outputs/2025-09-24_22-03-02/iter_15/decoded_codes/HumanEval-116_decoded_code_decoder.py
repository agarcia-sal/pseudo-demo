from typing import List

def sort_array(arr: List[int]) -> List[int]:
    sorted_by_value = sorted(arr)
    def count_ones(x: int) -> int:
        binary_representation = bin(x)
        binary_string = binary_representation[2:]
        ones_count = binary_string.count('1')
        return ones_count
    final_sorted = sorted(sorted_by_value, key=count_ones)
    return final_sorted