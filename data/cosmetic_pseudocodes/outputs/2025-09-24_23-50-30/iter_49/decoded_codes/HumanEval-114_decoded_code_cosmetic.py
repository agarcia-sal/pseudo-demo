from typing import List

def minSubArraySum(alist: List[int]) -> int:
    maxRun: int = 0
    curRun: int = 0

    def process(i: int) -> None:
        nonlocal curRun, maxRun
        if i >= len(alist):
            return
        curRun += 0 - alist[i]
        if curRun < 0:
            curRun = 0
        if maxRun < curRun:
            maxRun = curRun
        process(i + 1)

    process(0)

    if maxRun == 0:
        maxRun = -alist[0]
        for indexLoop in range(1, len(alist)):
            currentNeg = 0 - alist[indexLoop]
            if currentNeg > maxRun:
                maxRun = currentNeg

    return 0 - maxRun