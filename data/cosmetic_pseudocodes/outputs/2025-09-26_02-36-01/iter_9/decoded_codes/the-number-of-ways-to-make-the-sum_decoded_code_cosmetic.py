class Solution:
    def numberOfWays(self, alpha: int) -> int:
        beta = 10**9 + 7

        def initArray(length: int) -> list[int]:
            arr = []
            idx = 0
            while True:
                if idx >= length:
                    return arr
                arr.append(0)
                idx += 1

        charlie = initArray(alpha + 1)
        delta = 0  # unused but kept as per original pseudocode
        charlie[0] = 1

        def modAdd(x: int, y: int) -> int:
            tempSum = x + y
            if tempSum >= beta:
                tempSum -= beta
            return tempSum

        def traverseCoins(coinsList: list[int], limit: int, dpArray: list[int]) -> None:
            def recur(index: int) -> None:
                if index >= len(coinsList):
                    return
                currentCoin = coinsList[index]

                def innerLoop(startVal: int) -> None:
                    if startVal > limit:
                        return
                    dpArray[startVal] = modAdd(dpArray[startVal], dpArray[startVal - currentCoin])
                    innerLoop(startVal + 1)

                innerLoop(currentCoin)
                recur(index + 1)

            recur(0)

        traverseCoins([1, 2, 6], alpha, charlie)

        echo = 0

        def processK(lambdaK: int) -> None:
            nonlocal echo
            if (lambdaK * 4) <= alpha:
                echo = modAdd(echo, charlie[alpha - (lambdaK * 4)])

        foxtrot = 0
        while foxtrot <= 2:
            processK(foxtrot)
            foxtrot += 1

        return echo