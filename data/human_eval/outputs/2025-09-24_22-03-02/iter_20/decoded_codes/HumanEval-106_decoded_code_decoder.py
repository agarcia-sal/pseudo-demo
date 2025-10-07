from typing import List

def f(n: int) -> List[int]:
    ret: List[int] = []
    i = 1
    while i <= n:
        remainder = i % 2
        if remainder == 0:
            x = 1
            j = 1
            while j <= i:
                x *= j
                j += 1
            ret.append(x)
        else:
            x = 0
            j = 1
            while j <= i:
                x += j
                j += 1
            ret.append(x)
        i += 1
    return ret