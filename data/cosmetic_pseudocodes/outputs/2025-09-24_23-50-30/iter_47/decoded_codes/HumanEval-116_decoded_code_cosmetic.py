from typing import List


def sort_array(array_of_integers: List[int]) -> List[int]:
    def count_ones(binary_string: str) -> int:
        return sum(1 for ch in binary_string if ch == '1')

    temp_sorted_array = sorted(array_of_integers)

    def bit_count_key(element: int) -> int:
        bit_string = bin(element)
        bit_substring = bit_string[3:]  # substring from index 3 onward
        return count_ones(bit_substring)

    result_array = sorted(temp_sorted_array, key=bit_count_key)
    return result_array