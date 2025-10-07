from typing import List

def sort_array(array_of_integers: List[int]) -> List[int]:
    ordered_by_value: List[int] = sorted(array_of_integers)

    def count_ones_in_binary(num: int) -> int:
        binary_string = bin(num)
        # Skip '0b' prefix; count '1's from index 2 onwards
        ones_counter = 0
        index = 2
        while index < len(binary_string):
            if binary_string[index] == '1':
                ones_counter += 1
            index += 1
        return ones_counter

    # Sort by number of '1's in binary representation,
    # preserving ascending numerical order for ties
    sorted_by_ones = sorted(ordered_by_value, key=count_ones_in_binary)

    return sorted_by_ones