class Solution:
    def maxCollectedFruits(self, fruits):
        length_fruits = len(fruits)

        vectorA = [(1, 1), (1, 0)]
        vectorB = [(1, 0), (1, -1), (1, 1)]
        vectorC = [(-1, 1), (0, 1), (1, 1)]

        cacheMap = {}

        INF_NEG = -(10**9 + 7)

        def dp(alphaX, alphaY, betaX, betaY, gammaX, gammaY):
            if not (0 <= alphaX < length_fruits):
                return INF_NEG
            if not (0 <= alphaY < length_fruits):
                return INF_NEG
            if not (0 <= betaX < length_fruits):
                return INF_NEG
            if not (0 <= betaY < length_fruits):
                return INF_NEG
            if not (0 <= gammaX < length_fruits):
                return INF_NEG
            if not (0 <= gammaY < length_fruits):
                return INF_NEG

            terminalCond = (
                alphaX == alphaY == betaX == betaY == gammaX == gammaY == length_fruits - 1
            )
            if terminalCond:
                return fruits[length_fruits - 1][length_fruits - 1]

            keyTuple = (alphaX, alphaY, betaX, betaY, gammaX, gammaY)
            if keyTuple in cacheMap:
                return cacheMap[keyTuple]

            gatheredFruits = fruits[alphaX][alphaY]

            if (alphaX == betaX and alphaY == betaY) or (alphaX == gammaX and alphaY == gammaY):
                gatheredFruits = 0

            if betaX == gammaX and betaY == gammaY:
                gatheredFruits += fruits[betaX][betaY]
            else:
                gatheredFruits += fruits[betaX][betaY] + fruits[gammaX][gammaY]

            bestFruits = INF_NEG

            def helperLoop3(k, move1X, move1Y, move2X, move2Y):
                nonlocal bestFruits
                if k == len(vectorC):
                    return
                move3X, move3Y = vectorC[k]
                candidateValue = dp(
                    alphaX + move1X,
                    alphaY + move1Y,
                    betaX + move2X,
                    betaY + move2Y,
                    gammaX + move3X,
                    gammaY + move3Y,
                )
                if candidateValue > bestFruits:
                    bestFruits = candidateValue
                helperLoop3(k + 1, move1X, move1Y, move2X, move2Y)

            def helperLoop2(j, move1X, move1Y):
                if j == len(vectorB):
                    return
                move2X, move2Y = vectorB[j]
                helperLoop3(0, move1X, move1Y, move2X, move2Y)
                helperLoop2(j + 1, move1X, move1Y)

            def helperLoop1(i):
                if i == len(vectorA):
                    return
                move1X, move1Y = vectorA[i]
                helperLoop2(0, move1X, move1Y)
                helperLoop1(i + 1)

            helperLoop1(0)

            cacheSum = gatheredFruits + bestFruits
            cacheMap[keyTuple] = cacheSum
            return cacheSum

        return dp(0, 0, 0, length_fruits - 1, length_fruits - 1, 0)