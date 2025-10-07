from typing import List

def get_positive(l: List[int]) -> List[int]:
    result: List[int] = []
    for i in range(len(l)):
        e = l[i]
        if e > 0:
            result.append(e)
    return result