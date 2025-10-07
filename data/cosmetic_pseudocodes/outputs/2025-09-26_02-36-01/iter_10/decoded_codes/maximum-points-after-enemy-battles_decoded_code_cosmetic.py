from typing import List

class Solution:
    def maximumPoints(self, enemyEnergies: List[int], currentEnergy: int) -> int:
        def sortAscending(lst: List[int]) -> None:
            m = 0
            while m < len(lst) - 1:
                n = m + 1
                while n < len(lst):
                    if lst[m] > lst[n]:
                        lst[m], lst[n] = lst[n], lst[m]
                    n += 1
                m += 1

        sortAscending(enemyEnergies)

        if currentEnergy < enemyEnergies[0]:
            return 0

        tot = 0

        def loopDecrement(index: int) -> None:
            nonlocal tot, currentEnergy
            if index < 0:
                return
            tot += currentEnergy // enemyEnergies[0]
            currentEnergy = currentEnergy % enemyEnergies[0]
            currentEnergy += enemyEnergies[index]
            loopDecrement(index - 1)

        loopDecrement(len(enemyEnergies) - 1)

        return tot