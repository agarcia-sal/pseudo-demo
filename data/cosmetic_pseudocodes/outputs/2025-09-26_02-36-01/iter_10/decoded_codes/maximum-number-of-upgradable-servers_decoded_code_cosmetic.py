from typing import List

class Solution:
    def maxUpgrades(self, count: List[int], upgrade: List[int], sell: List[int], money: List[int]) -> List[int]:
        def computeMax(i: int, acc: List[int]) -> List[int]:
            if i > len(count) - 1:
                return acc

            xNum = count[i]
            yUpg = upgrade[i]
            zSel = sell[i]
            wMoney = money[i]

            def scanSell(j: int, maxFound: int) -> int:
                if j > xNum:
                    return maxFound
                remSrv = xNum - j
                sellVal = j * zSel
                totalCash = wMoney + sellVal
                candidateUpg = totalCash // yUpg
                if candidateUpg > remSrv:
                    candidateUpg = remSrv
                newMaxFound = maxFound
                if candidateUpg > maxFound:
                    newMaxFound = candidateUpg
                return scanSell(j + 1, newMaxFound)

            bestUpg = scanSell(0, 0)
            acc.append(bestUpg)
            return computeMax(i + 1, acc)

        return computeMax(0, [])