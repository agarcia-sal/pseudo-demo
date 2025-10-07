from typing import List


def sort_array(numbers_list: List[int]) -> List[int]:
    intermediate_sorted_list: List[int] = sorted(numbers_list)

    def binary_ones_counter(number: int) -> int:
        binary_rep: str = bin(number)[2:]
        ones_total: int = 0
        idx: int = 0
        while idx < len(binary_rep):
            if binary_rep[idx] == '1':
                ones_total += 1
            idx += 1
        return ones_total

    output_sorted_list: List[int] = sorted(intermediate_sorted_list, key=binary_ones_counter)
    return output_sorted_list