from typing import List

def sort_array(arr: List[int]) -> List[int]:
    return sorted(arr, key=lambda element: (bin(element).count('1'), element))