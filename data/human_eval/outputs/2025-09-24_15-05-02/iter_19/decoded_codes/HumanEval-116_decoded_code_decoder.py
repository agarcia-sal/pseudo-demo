from typing import List

def sort_array(array: List[int]) -> List[int]:
    return sorted(array, key=lambda x: (x, bin(x).count('1')))