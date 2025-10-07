from typing import List

class Solution:
    def maxUpgrades(self, count: List[int], upgrade: List[int], sell: List[int], money: List[int]) -> List[int]:
        def computeMax(A: int, B: int, C: int, D: int) -> int:
            maximum = 0
            for iterator in range(A + 1):
                remainingUnits = A - iterator
                gainMoney = iterator * C
                totalCash = D + gainMoney

                upgradesPossible = totalCash // B
                if upgradesPossible > remainingUnits:
                    upgradesPossible = remainingUnits

                if upgradesPossible > maximum:
                    maximum = upgradesPossible
            return maximum

        result = []
        for pos in range(len(count)):
            val = computeMax(count[pos], upgrade[pos], sell[pos], money[pos])
            result.append(val)

        return result