from typing import List

def minSubArraySum(array: List[int]) -> int:
    maxSumFound: int = 0
    currSum: int = 0
    index: int = 0
    length: int = len(array)

    while index < length:
        currSum += -array[index]
        if currSum < 0:
            currSum = 0
        if currSum > maxSumFound:
            maxSumFound = currSum
        index += 1

    if maxSumFound == 0:
        maxElem: int = -array[0]
        pos: int = 1
        while pos < length:
            negVal = -array[pos]
            if negVal > maxElem:
                maxElem = negVal
            pos += 1
        maxSumFound = maxElem

    result: int = -maxSumFound
    return result