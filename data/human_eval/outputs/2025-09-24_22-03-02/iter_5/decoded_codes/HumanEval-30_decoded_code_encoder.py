from typing import List

def get_positive(l: List[int]) -> List[int]:
    result = []
    for e in l:
        if e > 0:
            result.append(e)
    return result