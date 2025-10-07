from typing import List

def sort_array(list_numbers: List[int]) -> List[int]:
    first_pass = sorted(list_numbers)

    def count_ones(binary_text: str) -> int:
        return sum(1 for char in binary_text if char == '1')

    # Sort by number of '1's in binary representation without '0b' prefix
    result = sorted(first_pass, key=lambda item: count_ones(bin(item)[2:]))
    return result