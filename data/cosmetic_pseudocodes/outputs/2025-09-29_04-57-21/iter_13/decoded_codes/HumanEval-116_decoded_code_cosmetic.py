from typing import List

def sort_array(array_of_integers: List[int]) -> List[int]:
    interim_sorted: List[int] = sorted(array_of_integers)

    def count_ones_in_binary(number: int) -> int:
        # Count '1's in the binary representation of number (excluding the '0b' prefix)
        return sum(ch == '1' for ch in bin(number)[2:])

    output_array: List[int] = sorted(interim_sorted, key=count_ones_in_binary)
    return output_array