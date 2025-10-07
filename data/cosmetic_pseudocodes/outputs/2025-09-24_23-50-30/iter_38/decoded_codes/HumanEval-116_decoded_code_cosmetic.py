from typing import List

def sort_array(list_of_numbers: List[int]) -> List[int]:
    temp_sequence: List[int] = sorted(list_of_numbers)
    # Sort by count of '1's in binary representation starting from position 3 (0-based)
    reordered_sequence: List[int] = sorted(
        temp_sequence,
        key=lambda element: bin(element)[3:].count('1')
    )
    return reordered_sequence