from typing import List

def sort_array(array_of_non_negative_integers: List[int]) -> List[int]:
    return sorted(array_of_non_negative_integers, key=lambda x: (bin(x).count('1'), x))