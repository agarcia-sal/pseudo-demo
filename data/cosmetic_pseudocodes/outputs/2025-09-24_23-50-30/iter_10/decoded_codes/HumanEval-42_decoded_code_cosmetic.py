from typing import List

def incr_list(elements: List[int]) -> List[int]:
    result: List[int] = []
    index: int = 0
    while index < len(elements):
        result.append(elements[index] + 1)
        index += 1
    return result