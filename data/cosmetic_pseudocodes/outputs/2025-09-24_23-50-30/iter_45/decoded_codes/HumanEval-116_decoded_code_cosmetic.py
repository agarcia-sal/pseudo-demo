from typing import List


def sort_array(array_of_integers: List[int]) -> List[int]:
    def count_ones(binary_string: str) -> int:
        return sum(1 for char in binary_string if char == '1')

    temporary_sorted_array: List[int] = sorted(array_of_integers)

    def binary_ones_key(element: int) -> int:
        binary_str = bin(element)
        # slice from index 3 to end as per pseudocode (2-based index substring start)
        return count_ones(binary_str[3:])

    output_array: List[int] = sorted(temporary_sorted_array, key=binary_ones_key)
    return output_array