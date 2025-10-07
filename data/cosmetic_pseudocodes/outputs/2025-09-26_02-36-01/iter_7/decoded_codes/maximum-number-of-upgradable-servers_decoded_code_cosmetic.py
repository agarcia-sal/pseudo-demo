from typing import List

class Solution:
    def maxUpgrades(self, count: List[int], upgrade: List[int], sell: List[int], money: List[int]) -> List[int]:
        results = []
        totalItems = len(count)
        currIndex = 0

        while currIndex < totalItems:
            serversCount = count[currIndex]
            costForUpgrade = upgrade[currIndex]
            sellValue = sell[currIndex]
            availableMoney = money[currIndex]

            highestUpgradeCount = 0
            sellIterations = 0

            while sellIterations <= serversCount:
                serversLeft = serversCount - sellIterations
                gainFromSelling = sellIterations * sellValue
                combinedMoney = availableMoney + gainFromSelling

                upgradePossible = combinedMoney // costForUpgrade  # Use integer division
                if upgradePossible > serversLeft:
                    upgradePossible = serversLeft

                if highestUpgradeCount < upgradePossible:
                    highestUpgradeCount = upgradePossible

                sellIterations += 1

            results.append(highestUpgradeCount)
            currIndex += 1

        return results