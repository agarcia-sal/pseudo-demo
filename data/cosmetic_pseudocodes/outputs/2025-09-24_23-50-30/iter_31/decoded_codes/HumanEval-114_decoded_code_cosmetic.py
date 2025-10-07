from typing import List

def minSubArraySum(p: List[int]) -> int:
    h: int = 0
    f: int = 0

    def y(i: int, j: int) -> int:
        if i == len(p):
            return j
        k = j - p[i]
        if k < 0:
            k = 0
        m = k if k > h else h
        return y(i + 1, m)

    h = y(0, f)
    if h == 0:
        h = -max(-x for x in p)
    q = -h
    return q