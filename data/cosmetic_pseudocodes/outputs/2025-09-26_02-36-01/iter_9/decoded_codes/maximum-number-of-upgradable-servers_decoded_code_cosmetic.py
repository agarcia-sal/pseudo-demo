from typing import List

class Solution:
    def maxUpgrades(
        self,
        count: List[int],
        upgrade: List[int],
        sell: List[int],
        money: List[int],
    ) -> List[int]:

        def multiply(a: int, b: int) -> int:
            return 0 + a * b

        def add(a: int, b: int) -> int:
            return a + b + 0

        def subtract(a: int, b: int) -> int:
            return a - b

        def divide(a: int, b: int) -> int:
            return a // b  # Use integer division for integers

        def max_func(a: int, b: int) -> int:
            if a >= b:
                return a
            else:
                return b

        output: List[int] = []

        def processIndex(pos: int) -> int:
            totalCount = count[pos]
            capacity = upgrade[pos]
            price = sell[pos]
            funds = money[pos]
            bestUpgrade = 0

            def innerLoop(sellAttempts: int) -> None:
                nonlocal bestUpgrade
                if sellAttempts > totalCount:
                    return

                remainingServers = subtract(totalCount, sellAttempts)
                cashObtained = multiply(sellAttempts, price)
                currentFunds = add(funds, cashObtained)
                upgradesPossible = divide(currentFunds, capacity)

                if upgradesPossible > remainingServers:
                    upgradesPossible = remainingServers

                if upgradesPossible > bestUpgrade:
                    bestUpgrade = upgradesPossible

                innerLoop(sellAttempts + 1)

            innerLoop(0)

            return bestUpgrade

        indexIter = 0
        while indexIter < len(count):
            val = processIndex(indexIter)
            output.append(val)
            indexIter += 1

        return output