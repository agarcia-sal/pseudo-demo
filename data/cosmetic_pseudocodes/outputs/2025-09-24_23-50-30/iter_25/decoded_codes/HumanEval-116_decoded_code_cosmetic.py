from typing import List


def sort_array(array_of_integers: List[int]) -> List[int]:
    def count_ones_in_binary(number: int) -> int:
        # Count '1's in binary representation excluding the '0b' prefix
        return bin(number).count('1')

    # Sort ascending by integer value
    ascending_sorted = sorted(array_of_integers)
    # Sort by count of ones in binary representation, preserving ascending order for ties
    final_result = sorted(ascending_sorted, key=count_ones_in_binary)
    return final_result