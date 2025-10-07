from typing import List

def sort_array(array_of_integers: List[int]) -> List[int]:
    # Sort ascending first
    interim_list: List[int] = sorted(array_of_integers)
    # Then sort by count of '1's in binary representation (excluding '0b' prefix)
    result_list: List[int] = sorted(
        interim_list,
        key=lambda element: sum(ch == '1' for ch in bin(element)[2:])
    )
    return result_list