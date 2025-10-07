from typing import List

def sort_array(arr: List[int]) -> List[int]:
    return sorted(arr, key=lambda x: (x, bin(x).count('1')))