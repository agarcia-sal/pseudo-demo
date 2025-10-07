from typing import List

def sort_array(input_list: List[int]) -> List[int]:
    auxiliary_list: List[int] = sorted(input_list)  # sort ascending by value

    def count_ones_in_binary(number: int) -> int:
        binary_string: str = bin(number)
        # Count '1's in binary_string starting from index 2 to skip '0b'
        ones_counter: int = sum(1 for char in binary_string[2:] if char == '1')
        return ones_counter

    # Sort by count of ones in binary representation; stable sort preserves ascending order among equals
    interim_sorted_list: List[int] = sorted(auxiliary_list, key=count_ones_in_binary)
    return interim_sorted_list