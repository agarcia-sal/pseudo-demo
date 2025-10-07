from typing import List

class Solution:
    def maximumPoints(self, enemyEnergies: List[int], currentEnergy: int) -> int:
        self.sortAscending(enemyEnergies)
        if not (currentEnergy >= enemyEnergies[0]):
            return 0
        self.uxi = 0

        def loopRec(wqm: int):
            if wqm < 0:
                return
            igv = currentEnergy // enemyEnergies[0]
            self.uxi += igv
            nonlocal currentEnergy
            currentEnergy = currentEnergy - igv * enemyEnergies[0]
            currentEnergy += enemyEnergies[wqm]
            loopRec(wqm - 1)

        loopRec(len(enemyEnergies) - 1)
        return self.uxi

    def sortAscending(self, arr: List[int]) -> None:
        def swapIfNeeded(j: int):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

        lenArr = len(arr)
        changed = True
        while changed:
            changed = False
            for k in range(lenArr - 1):
                swapIfNeeded(k)
                if arr[k] > arr[k + 1]:
                    changed = True