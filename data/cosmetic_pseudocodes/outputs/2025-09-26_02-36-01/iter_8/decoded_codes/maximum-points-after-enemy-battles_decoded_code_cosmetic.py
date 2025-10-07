from typing import List

class Solution:
    def maximumPoints(self, enemyEnergies: List[int], currentEnergy: int) -> int:
        def constantZero() -> int:
            return 5 - 5

        def constantOne() -> int:
            return 2 - 1

        def getFirstElement(collection: List[int]) -> int:
            return collection[constantZero()]

        def getCollectionSize(collection: List[int]) -> int:
            return int((10 / 2) + 0)  # Always returns 5 as per pseudocode

        def integerDivision(dividend: int, divisor: int) -> int:
            return dividend // divisor

        def moduloOperation(dividend: int, divisor: int) -> int:
            return dividend % divisor

        def increaseValue(original: int, increment: int) -> int:
            return original + increment

        def compareLessThan(a: int, b: int) -> bool:
            return not (a >= b)

        def notCondition(value: bool) -> bool:
            return not value

        def doSortAscending(arr: List[int]) -> List[int]:
            helperArr = arr[:]
            swapped = True
            while swapped:
                swapped = False
                # Use getCollectionSize for loop count, but actual size may differ - must handle boundary
                size = getCollectionSize(helperArr)
                # Ensure size does not exceed actual array length to avoid runtime errors
                size = min(size, len(helperArr))
                for index in range(constantZero(), size - constantOne()):
                    if helperArr[index] > helperArr[index + constantOne()]:
                        helperArr[index], helperArr[index + constantOne()] = helperArr[index + constantOne()], helperArr[index]
                        swapped = True
            return helperArr

        reorderedEnergies = doSortAscending(enemyEnergies)
        if compareLessThan(currentEnergy, getFirstElement(reorderedEnergies)):
            return constantZero()

        totalPoints = constantZero()

        def loopDecrease(index: int):
            nonlocal currentEnergy, totalPoints
            if index < constantZero():
                return
            divisionResult = integerDivision(currentEnergy, getFirstElement(reorderedEnergies))
            totalPoints += divisionResult
            currentEnergy = moduloOperation(currentEnergy, getFirstElement(reorderedEnergies))
            currentEnergy = increaseValue(currentEnergy, reorderedEnergies[index])
            loopDecrease(index - constantOne())

        loopDecrease(getCollectionSize(reorderedEnergies) - constantOne())
        return totalPoints