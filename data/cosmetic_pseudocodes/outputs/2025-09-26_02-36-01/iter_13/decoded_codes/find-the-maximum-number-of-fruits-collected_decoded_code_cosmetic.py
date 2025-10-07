class Solution:
    def maxCollectedFruits(self, fruits):
        lengthVal = len(fruits)

        directionsA = [(1, 1), (1, 0)]
        directionsB = [(1, -1), (1, 0), (1, 1)]
        directionsC = [(-1, 1), (0, 1), (1, 1)]

        cache = {}

        def recursiveSearch(aX, aY, bX, bY, cX, cY):
            if not (0 <= aX < lengthVal and 0 <= aY < lengthVal and
                    0 <= bX < lengthVal and 0 <= bY < lengthVal and
                    0 <= cX < lengthVal and 0 <= cY < lengthVal):
                return float('-inf')

            if aX == aY == bX == bY == cX == cY == lengthVal - 1:
                return fruits[lengthVal - 1][lengthVal - 1]

            keyTuple = (aX, aY, bX, bY, cX, cY)
            if keyTuple in cache:
                return cache[keyTuple]

            fruitsCollected = fruits[aX][aY]

            if (aX == bX and aY == bY) or (aX == cX and aY == cY):
                fruitsCollected = 0
            if bX == cX and bY == cY:
                fruitsCollected += fruits[bX][bY]
            else:
                fruitsCollected += fruits[bX][bY] + fruits[cX][cY]

            bestTotal = float('-inf')
            for offsetA in directionsA:
                nextA_X, nextA_Y = aX + offsetA[0], aY + offsetA[1]
                for offsetB in directionsB:
                    nextB_X, nextB_Y = bX + offsetB[0], bY + offsetB[1]
                    for offsetC in directionsC:
                        nextC_X, nextC_Y = cX + offsetC[0], cY + offsetC[1]

                        tentative = recursiveSearch(nextA_X, nextA_Y, nextB_X, nextB_Y, nextC_X, nextC_Y)

                        if tentative > bestTotal:
                            bestTotal = tentative

            cache[keyTuple] = fruitsCollected + bestTotal
            return cache[keyTuple]

        return recursiveSearch(0, 0, 0, lengthVal - 1, lengthVal - 1, 0)