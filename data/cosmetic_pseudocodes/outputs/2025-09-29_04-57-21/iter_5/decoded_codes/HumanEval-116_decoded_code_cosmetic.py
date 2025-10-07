from typing import List

def sort_array(array_of_integers: List[int]) -> List[int]:
    list_ordered_numbers: List[int] = sorted(array_of_integers)

    def bitcount(value: int) -> int:
        # Count number of '1's in binary representation excluding the '0b' prefix
        bits_string: str = bin(value)
        return sum(1 for char in bits_string[2:] if char == '1')

    # Sort primarily by bitcount, stable sort so ties preserve ascending numerical order
    return sorted(list_ordered_numbers, key=bitcount)