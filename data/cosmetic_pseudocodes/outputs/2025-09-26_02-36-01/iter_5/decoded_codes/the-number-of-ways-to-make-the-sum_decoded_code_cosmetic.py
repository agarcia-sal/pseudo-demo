class Solution:
    def numberOfWays(self, m: int) -> int:
        constantModulus = 10**9 + 7
        counterList = [0] * (m + 1)
        counterList[0] = 1

        coinsArray = [1, 2, 6]

        def processCoin(idx: int) -> None:
            if idx >= 3:
                return

            currentCoin = coinsArray[idx]

            def loopIncrement(pos: int) -> None:
                if pos > m:
                    return
                leftValue = counterList[pos]
                rightValue = counterList[pos - currentCoin]
                counterList[pos] = (leftValue + rightValue) % constantModulus
                loopIncrement(pos + 1)

            loopIncrement(currentCoin)
            processCoin(idx + 1)

        processCoin(0)

        accumulatorResult = 0

        def sumOverK(kVal: int) -> None:
            nonlocal accumulatorResult
            if kVal > 2:
                return
            if not (kVal * 4 > m):
                tempIndex = m - (4 * kVal)
                accumulatorResult = (accumulatorResult + counterList[tempIndex]) % constantModulus
            sumOverK(kVal + 1)

        sumOverK(0)

        return accumulatorResult