from typing import List

def get_positive(l: List) -> List:
    result = []
    for i in range(len(l)):
        e = l[i]
        if e > 0:
            result.append(e)
    return result