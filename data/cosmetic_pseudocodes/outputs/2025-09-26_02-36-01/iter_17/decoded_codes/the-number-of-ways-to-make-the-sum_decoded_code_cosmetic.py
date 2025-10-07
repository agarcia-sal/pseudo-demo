class Solution:
    def numberOfWays(self, n: int) -> int:
        CONST_MODULO = 10**9 + 7
        dpArray = [0] * (n + 1)
        dpArray[0] = 1

        coinsList = [1, 2, 6]
        for currentCoin in coinsList:
            for iteratorJ in range(currentCoin, n + 1):
                dpArray[iteratorJ] = (dpArray[iteratorJ] + dpArray[iteratorJ - currentCoin]) % CONST_MODULO

        accumulator = 0
        for idxK in range(3):
            if idxK * 4 <= n:
                subIndex = n - idxK * 4
                accumulator = (accumulator + dpArray[subIndex]) % CONST_MODULO

        return accumulator