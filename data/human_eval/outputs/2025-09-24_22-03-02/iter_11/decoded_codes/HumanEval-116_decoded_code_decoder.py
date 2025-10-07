from typing import List

def sort_array(arr: List[int]) -> List[int]:
    return sorted(sorted(arr), key=lambda x: bin(x)[2:].count('1'))