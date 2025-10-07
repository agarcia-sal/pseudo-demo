from typing import List

def get_positive(l: List[int]) -> List[int]:
    result = []
    for element in l:
        if element > 0:
            result.append(element)
    return result