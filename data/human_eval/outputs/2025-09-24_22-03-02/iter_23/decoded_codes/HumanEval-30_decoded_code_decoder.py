from typing import List

def get_positive(l: List[int]) -> List[int]:
    result = []
    index = 0
    while index < len(l):
        e = l[index]
        if e > 0:
            result.append(e)
        index += 1
    return result