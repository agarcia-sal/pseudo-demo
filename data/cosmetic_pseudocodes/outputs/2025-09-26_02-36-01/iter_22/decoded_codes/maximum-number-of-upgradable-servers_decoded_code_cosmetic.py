from typing import List

class Solution:
    def maxUpgrades(self, count: List[int], upgrade: List[int], sell: List[int], money: List[int]) -> List[int]:
        result = []
        pos = 0
        n = len(count)
        while pos < n:
            curCount = count[pos]
            costUpgrade = upgrade[pos]
            priceSell = sell[pos]
            cashStart = money[pos]
            topUpgrade = 0
            i = 0
            while i <= curCount:
                serversLeft = curCount - i
                incomeSell = i * priceSell
                totalCash = cashStart + incomeSell
                possible = totalCash // costUpgrade
                if possible > serversLeft:
                    possible = serversLeft
                if possible > topUpgrade:
                    topUpgrade = possible
                i += 1
            result.append(topUpgrade)
            pos += 1
        return result