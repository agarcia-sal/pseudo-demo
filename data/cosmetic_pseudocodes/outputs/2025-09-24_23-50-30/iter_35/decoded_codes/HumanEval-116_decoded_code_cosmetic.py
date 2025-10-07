from typing import List

def sort_array(list_of_ints: List[int]) -> List[int]:
    def key_function(value: int) -> int:
        # Convert to binary, slice off the '0b' prefix and the first two characters after that (i.e., skip first 3 chars)
        # Count '1's in the remaining substring
        binary_str = bin(value)[2:]  # binary representation without '0b'
        # According to pseudocode, slice from index 3 onwards
        return sum(1 for char in binary_str[3:] if char == '1')

    first_sorted = sorted(list_of_ints)
    second_sorted = sorted(first_sorted, key=key_function)
    return second_sorted