from typing import List

def search(mList: List[int]) -> int:
    freqArr: List[int] = [0] * (max(mList) + 1)
    mCounter: int = 0
    while mCounter < len(mList):
        freqArr[mList[mCounter]] += 1
        mCounter += 1
    resVal: int = -1
    idxIter: int = 1
    while idxIter < len(freqArr):
        if freqArr[idxIter] >= idxIter:
            resVal = idxIter
        idxIter += 1
    return resVal