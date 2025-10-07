from typing import List

def sort_array(numbers_list: List[int]) -> List[int]:
    def compare_ones(num: int) -> int:
        binary_string = bin(num)[2:]
        count_ones = sum(1 for char in binary_string if char == '1')
        return count_ones

    ascending_sorted = sorted(numbers_list)
    result_sorted = sorted(ascending_sorted, key=compare_ones)
    return result_sorted