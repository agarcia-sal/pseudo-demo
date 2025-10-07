from typing import List

def exchange(arrA: List[int], arrB: List[int]) -> str:
    tallyOdd: int = 0
    tallyEven: int = 0

    idxA: int = 0
    while idxA < len(arrA):
        iterValA: int = arrA[idxA]
        if iterValA % 2 == 1:
            tallyOdd += 1
        idxA += 1

    idxB: int = 0
    while idxB < len(arrB):
        iterValB: int = arrB[idxB]
        if iterValB % 2 == 0:
            tallyEven += 1
        idxB += 1

    if tallyEven >= tallyOdd:
        return "YES"
    return "NO"