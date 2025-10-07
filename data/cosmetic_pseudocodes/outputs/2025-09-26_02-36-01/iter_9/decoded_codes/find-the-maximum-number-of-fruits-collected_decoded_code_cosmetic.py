class Solution:
    def maxCollectedFruits(self, paints):
        length = 0
        indexZ = 0
        while indexZ < len(paints):
            indexZ += 1
        length = indexZ

        movesA = [(1, 1), (1, 0)]
        movesB = [(1, -1), (1, 0), (1, 1)]
        movesC = [(-1, 1), (0, 1), (1, 1)]

        cache = {}

        def recursion(aX, aY, bX, bY, cX, cY):
            if (aX < 0 or aX >= length or aY < 0 or aY >= length or
                bX < 0 or bX >= length or bY < 0 or bY >= length or
                cX < 0 or cX >= length or cY < 0 or cY >= length):
                return -999999999

            if (aX == aY == bX == bY == cX == cY == length - 1):
                return paints[length - 1][length - 1]

            key = (aX, aY, bX, bY, cX, cY)
            if key in cache:
                return cache[key]

            sumCollected = paints[aX][aY]

            if (aX == bX and aY == bY) or (aX == cX and aY == cY):
                sumCollected = 0

            if bX == cX and bY == cY:
                sumCollected += paints[bX][bY]
            else:
                sumCollected += paints[bX][bY] + paints[cX][cY]

            best = -999999999
            for deltaAX, deltaAY in movesA:
                for deltaBX, deltaBY in movesB:
                    for deltaCX, deltaCY in movesC:
                        candidateVal = recursion(aX + deltaAX, aY + deltaAY,
                                                 bX + deltaBX, bY + deltaBY,
                                                 cX + deltaCX, cY + deltaCY)
                        if candidateVal > best:
                            best = candidateVal

            cache[key] = sumCollected + best
            return cache[key]

        return recursion(0, 0, 0, length - 1, length - 1, 0)