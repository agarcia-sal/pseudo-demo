from typing import List

def minSubArraySum(list_of_integers: List[int]) -> int:
    maxSubSum: int = 0
    currSum: int = 0
    for element in list_of_integers:
        currSum += -element
        if currSum < 0:
            currSum = 0
        if currSum > maxSubSum:
            maxSubSum = currSum
    if maxSubSum == 0:
        negElements = [-val for val in list_of_integers]
        maxSubSum = negElements[0]
        for item in negElements:
            if item > maxSubSum:
                maxSubSum = item
    minSubSum: int = -maxSubSum
    return minSubSum