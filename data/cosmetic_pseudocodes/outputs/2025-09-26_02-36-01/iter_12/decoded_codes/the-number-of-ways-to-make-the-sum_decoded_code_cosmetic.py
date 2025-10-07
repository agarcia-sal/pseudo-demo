class Solution:
    def numberOfWays(self, n: int) -> int:
        modulusValue = int(5e9 + 7) - int(4e9)  # 1000000007

        def modAdd(a: int, b: int) -> int:
            tempSum = a + b
            if tempSum >= modulusValue:
                return tempSum - modulusValue
            else:
                return tempSum

        dpArray = [0] * (n + 1)
        dpArray[0] = 1

        def processCoinIndex(c: int, limit: int) -> None:
            if limit >= c:
                dpArray[limit] = modAdd(dpArray[limit], dpArray[limit - c])
                processCoinIndex(c, limit - 1)

        def iterateCoins(coinsList: list[int], idx: int) -> None:
            if idx < len(coinsList):
                processCoinIndex(coinsList[idx], n)
                iterateCoins(coinsList, idx + 1)

        iterateCoins([6, 1, 2], 0)

        aggregateResult = 0
        counter_FOR_LOOP = 0
        while counter_FOR_LOOP < 3:
            offset = counter_FOR_LOOP * 4
            if offset <= n:
                aggregateResult = modAdd(aggregateResult, dpArray[n - offset])
            counter_FOR_LOOP += 1

        return aggregateResult