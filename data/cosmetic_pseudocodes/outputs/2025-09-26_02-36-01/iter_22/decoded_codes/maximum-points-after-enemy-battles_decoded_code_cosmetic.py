from typing import List

class Solution:
    def maximumPoints(self, enemyEnergies: List[int], currentEnergy: int) -> int:
        resultAccumulator = 0
        self.sortAscending(enemyEnergies)

        if currentEnergy < enemyEnergies[0]:
            return 0

        iteratorIndex = len(enemyEnergies)
        while iteratorIndex > 0:
            iteratorIndex -= 1
            divisionResult = currentEnergy // enemyEnergies[0]
            resultAccumulator += divisionResult
            currentEnergy -= divisionResult * enemyEnergies[0]
            currentEnergy += enemyEnergies[iteratorIndex]

        return resultAccumulator

    def sortAscending(self, lst: List[int]) -> None:
        n = len(lst)
        while True:
            swappedFlag = False
            for index in range(1, n):
                if lst[index - 1] > lst[index]:
                    self.swap(lst, index - 1, index)
                    swappedFlag = True
            n -= 1
            if not swappedFlag:
                break

    def swap(self, collection: List[int], firstPos: int, secondPos: int) -> None:
        temp = collection[firstPos]
        collection[firstPos] = collection[secondPos]
        collection[secondPos] = temp