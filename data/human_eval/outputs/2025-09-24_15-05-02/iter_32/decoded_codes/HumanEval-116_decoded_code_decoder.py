from typing import List

def sort_array(array_of_integers: List[int]) -> List[int]:
    # Sort by integer value ascending, then by count of '1's in binary representation ascending
    return sorted(
        sorted(array_of_integers),
        key=lambda number: bin(number).count('1')
    )