class Solution:
    def numberOfWays(self, n: int) -> int:
        P = 10**9 + 7
        dpArray = [0] * (n + 1)
        dpArray[0] = 1
        coinsArray = [1, 2, 6]

        def processCoin(c: int, limit: int, arr: list, modVal: int) -> None:
            for idx in range(c, limit + 1):
                arr[idx] = (arr[idx] + arr[idx - c]) % modVal

        for currCoin in coinsArray:
            processCoin(currCoin, n, dpArray, P)

        totalWays = 0
        for counter in range(3):
            if counter * 4 <= n:
                totalWays = (totalWays + dpArray[n - counter * 4]) % P

        return totalWays