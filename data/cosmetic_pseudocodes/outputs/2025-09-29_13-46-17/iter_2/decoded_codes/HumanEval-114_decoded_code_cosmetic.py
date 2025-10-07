from typing import List

def minSubArraySum(list_of_integers: List[int]) -> int:
    maxSum: int = 0
    tempSum: int = 0

    def recursive_process(index: int) -> None:
        nonlocal maxSum, tempSum
        if index == len(list_of_integers):
            return
        currentVal = -list_of_integers[index]
        tempSum = 0 if (tempSum + currentVal) < 0 else (tempSum + currentVal)
        maxSum = tempSum if tempSum > maxSum else maxSum
        recursive_process(index + 1)

    recursive_process(0)

    if maxSum == 0:
        maxSum = max(-x for x in list_of_integers)

    return -maxSum