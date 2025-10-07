import math
from typing import List

class Solution:
    def maximumPoints(self, enemyEnergies: List[int], currentEnergy: int) -> int:
        def sortAscending(arr: List[int]) -> None:
            def quicksort(left: int, right: int) -> None:
                if left >= right:
                    return
                pivotIndex = left
                pivotValue = arr[pivotIndex]
                low = left + 1
                high = right
                while low <= high:
                    while low <= right and arr[low] <= pivotValue:
                        low += 1
                    while high >= left and arr[high] >= pivotValue:
                        high -= 1
                    if low < high:
                        arr[low], arr[high] = arr[high], arr[low]
                arr[pivotIndex], arr[high] = arr[high], arr[pivotIndex]
                quicksort(left, high - 1)
                quicksort(high + 1, right)

            quicksort(0, len(arr) - 1)

        sortAscending(enemyEnergies)

        if currentEnergy < enemyEnergies[0]:
            return 0

        collected = 0
        lastIndex = len(enemyEnergies) - 1

        def recurse(idx: int, energy: int, acc: int) -> int:
            if idx < 0:
                return acc
            divResult = energy / enemyEnergies[0]
            intDiv = math.floor(divResult)
            modResult = energy - (enemyEnergies[0] * intDiv)
            newAcc = acc + intDiv
            nextEnergy = modResult + enemyEnergies[idx]
            return recurse(idx - 1, nextEnergy, newAcc)

        collected = recurse(lastIndex, currentEnergy, collected)

        return collected