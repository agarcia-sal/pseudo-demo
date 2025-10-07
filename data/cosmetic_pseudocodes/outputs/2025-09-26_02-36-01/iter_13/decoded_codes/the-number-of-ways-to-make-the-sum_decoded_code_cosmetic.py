class Solution:
    def numberOfWays(self, n: int) -> int:
        CONST_MOD = 10**9 + 7

        def helperAdd(a: int, b: int) -> int:
            return (a + b) % CONST_MOD

        def processCoin(index: int, coinsList: list[int], dpArray: list[int]) -> None:
            if index == len(coinsList):
                return

            currentCoin = coinsList[index]
            loopCounter = currentCoin
            while loopCounter <= n:
                dpArray[loopCounter] = helperAdd(dpArray[loopCounter], dpArray[loopCounter - currentCoin])
                loopCounter += 1

            processCoin(index + 1, coinsList, dpArray)

        coinList = [1, 2, 6]
        dpArr = [0] * (n + 1)
        dpArr[0] = 1

        processCoin(0, coinList, dpArr)

        resVal = 0
        kVal = 0
        while kVal <= 2:
            if (kVal * 4) <= n:
                resVal = helperAdd(resVal, dpArr[n - (kVal * 4)])
            kVal += 1

        return resVal