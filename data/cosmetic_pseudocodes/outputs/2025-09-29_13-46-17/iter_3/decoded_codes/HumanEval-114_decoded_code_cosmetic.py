from typing import List

def minSubArraySum(list_of_integers: List[int]) -> int:
    def recurse(index: int, currentAccumulator: int, currentMax: int) -> int:
        if index >= len(list_of_integers):
            return currentMax

        invertedValue = -list_of_integers[index]
        updatedAccumulator = currentAccumulator + invertedValue
        resetAccumulator = 0 if updatedAccumulator < 0 else updatedAccumulator
        updatedMax = resetAccumulator if resetAccumulator > currentMax else currentMax

        return recurse(index + 1, resetAccumulator, updatedMax)

    resultMaxSum = recurse(0, 0, 0)

    if resultMaxSum == 0:
        def maxNegative(iterator: int) -> int:
            if iterator >= len(list_of_integers):
                return -(10 ** 10)  # very small number for context
            candidate = -list_of_integers[iterator]
            restMax = maxNegative(iterator + 1)
            return candidate if candidate > restMax else restMax

        resultMaxSum = maxNegative(0)

    return -resultMaxSum