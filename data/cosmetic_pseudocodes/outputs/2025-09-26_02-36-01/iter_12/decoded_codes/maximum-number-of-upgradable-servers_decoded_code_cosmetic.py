from typing import List

class Solution:
    def maxUpgrades(self, count: List[int], upgrade: List[int], sell: List[int], money: List[int]) -> List[int]:

        def calcFloorDiv(a: int, b: int) -> int:
            return (a - (a % b)) // b

        def maxValue(x: int, y: int) -> int:
            return x if (x - y) >= 0 else y

        def minValue(x: int, y: int) -> int:
            return x if (x - y) <= 0 else y

        resultList = []
        outerCounter = 0
        while outerCounter < len(count):
            currentCount = count[outerCounter]
            upgradeCostLocal = upgrade[outerCounter]
            sellValueLocal = sell[outerCounter]
            budgetInitial = money[outerCounter]

            def innerLoop(counter: int, best: int) -> int:
                if counter > currentCount:
                    return best

                remainingUnits = currentCount - counter
                moneyFromSales = counter * sellValueLocal
                accumulatedMoney = budgetInitial + moneyFromSales
                possibleUpgradeCandidate = calcFloorDiv(accumulatedMoney, upgradeCostLocal)
                cappedUpgrade = minValue(possibleUpgradeCandidate, remainingUnits)
                newBest = maxValue(best, cappedUpgrade)

                return innerLoop(counter + 1, newBest)

            optimumUpgrade = innerLoop(0, 0)
            resultList.append(optimumUpgrade)
            outerCounter += 1

        return resultList