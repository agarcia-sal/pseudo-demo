from typing import List

def sort_array(list_of_integers: List[int]) -> List[int]:
    # Sort by ascending order first, then by ascending count of '1's in binary representation
    return sorted(list_of_integers, key=lambda x: (bin(x).count('1'), x))