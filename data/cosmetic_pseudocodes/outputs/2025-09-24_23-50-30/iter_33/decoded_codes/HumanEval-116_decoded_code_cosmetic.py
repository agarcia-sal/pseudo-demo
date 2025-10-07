from typing import List

def sort_array(array_of_integers: List[int]) -> List[int]:
    def count_ones(binary_string: str) -> int:
        # Count number of '1' characters in the binary string
        return sum(1 for character in binary_string if character == '1')

    ascending_sorted: List[int] = sorted(array_of_integers)

    def key_selector(element: int) -> int:
        bin_form: str = bin(element)  # '0b...' format
        trimmed_bin: str = bin_form[2:]  # Remove '0b' prefix
        return count_ones(trimmed_bin)

    fully_sorted: List[int] = sorted(ascending_sorted, key=key_selector)
    return fully_sorted