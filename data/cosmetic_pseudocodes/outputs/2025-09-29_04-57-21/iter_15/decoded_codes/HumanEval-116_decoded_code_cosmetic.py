from typing import List

def sort_array(array_of_integers: List[int]) -> List[int]:
    ascending_sorted: List[int] = sorted(array_of_integers)

    def count_ones(binary_string: str) -> int:
        total: int = 0
        index: int = 0
        length: int = len(binary_string)
        while index < length:
            if binary_string[index] == '1':
                total += 1
            index += 1
        return total

    def binary_ones_counter(element: int) -> int:
        binary_form: str = bin(element)[2:]  # Skip '0b' prefix
        return count_ones(binary_form)

    grouped_sorted: List[int] = sorted(ascending_sorted, key=binary_ones_counter)
    return grouped_sorted