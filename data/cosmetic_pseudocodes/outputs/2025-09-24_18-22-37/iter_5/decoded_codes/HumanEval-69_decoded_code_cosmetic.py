from typing import List

def search(list_of_integers: List[int]) -> int:
    maxVal: int = 0
    for idx in range(len(list_of_integers)):
        if list_of_integers[idx] > maxVal:
            maxVal = list_of_integers[idx]

    counts: List[int] = [0] * (maxVal + 1)

    position: int = 0
    while position < len(list_of_integers):
        currentNum: int = list_of_integers[position]
        counts[currentNum] += 1
        position += 1

    result: int = -1
    idxCheck: int = 1
    while idxCheck < len(counts):
        if counts[idxCheck] >= idxCheck:
            result = idxCheck
        idxCheck += 1

    return result