from typing import List

def monotonic(list_elements: List[int]) -> bool:
    return list_elements == sorted(list_elements) or list_elements == sorted(list_elements, reverse=True)