from typing import List

def sort_array(list_of_numbers: List[int]) -> List[int]:
    ascending_sorted_list: List[int] = sorted(list_of_numbers)

    def count_ones(item: int) -> int:
        binary_without_prefix: str = bin(item)[2:]
        count_of_ones: int = 0
        index_counter: int = 0
        while index_counter < len(binary_without_prefix):
            if binary_without_prefix[index_counter] == '1':
                count_of_ones += 1
            index_counter += 1
        return count_of_ones

    binary_ones_sorted_list: List[int] = sorted(ascending_sorted_list, key=count_ones)
    return binary_ones_sorted_list