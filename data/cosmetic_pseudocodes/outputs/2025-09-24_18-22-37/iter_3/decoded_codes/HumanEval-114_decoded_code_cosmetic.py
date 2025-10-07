from typing import List

def minSubArraySum(list_of_integers: List[int]) -> int:
    idx: int = 0
    tempSum: int = 0
    maxSumFound: int = 0
    length: int = len(list_of_integers)

    while idx < length:
        tempSum += -list_of_integers[idx]
        if tempSum < 0:
            tempSum = 0
        if tempSum > maxSumFound:
            maxSumFound = tempSum
        idx += 1

    if maxSumFound == 0:
        negElements: List[int] = [-x for x in list_of_integers]  # invert sign of elements
        maxNum: int = negElements[0]
        j: int = 1
        while j < length:
            if negElements[j] > maxNum:
                maxNum = negElements[j]
            j += 1
        maxSumFound = maxNum

    result: int = -maxSumFound
    return result