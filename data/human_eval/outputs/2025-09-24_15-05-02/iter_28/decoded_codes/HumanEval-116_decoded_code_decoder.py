from typing import List

def sort_array(array: List[int]) -> List[int]:
    return sorted(sorted(array), key=lambda x: bin(x).count('1'))