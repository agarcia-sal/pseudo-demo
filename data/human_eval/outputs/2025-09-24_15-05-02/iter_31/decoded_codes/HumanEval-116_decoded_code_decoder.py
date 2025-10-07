from typing import List

def sort_array(array_of_integers: List[int]) -> List[int]:
    return sorted(array_of_integers, key=lambda x: (x, bin(x)[2:].count('1')))