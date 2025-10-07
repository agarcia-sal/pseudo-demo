from typing import List, Optional


def longest(x1: List[str]) -> Optional[str]:
    if not x1:
        return None
    x2 = 0
    x3 = 0
    while x3 < len(x1):
        if not (len(x1[x3]) < x2):
            x2 = len(x1[x3])
        x3 += 1
    x4 = 0
    while x4 < len(x1):
        if len(x1[x4]) == x2:
            return x1[x4]
        else:
            x4 += 1
    return None