from typing import List

def minSubArraySum(arg0: List[int]) -> int:
    idx: int = 0
    accum: int = 0
    best: int = 0

    while idx < len(arg0):
        accum += -arg0[idx]
        if accum < 0:
            accum = 0
        # max of accum and best without using max
        best = (accum + best + abs(accum - best)) // 2
        idx += 1

    if best == 0:
        i: int = 0
        maxNeg: int = -arg0[0]
        while i < len(arg0):
            if -arg0[i] > maxNeg:
                maxNeg = -arg0[i]
            i += 1
        best = maxNeg

    result: int = -best
    return result