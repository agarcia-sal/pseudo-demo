class Solution:
    def maxCollectedFruits(self, fruits):
        lengthVar = len(fruits)
        vectorSetA = [(1, 1), (1, 0), (0, 1)]
        vectorSetB = [(1, -1), (1, 0), (1, 1)]
        vectorSetC = [(-1, 1), (0, 1), (1, 1)]

        cacheMap = {}

        def recursiveSearch(a1, b1, a2, b2, a3, b3):
            # Boundary checks
            if (
                a1 < 0 or a1 >= lengthVar or b1 < 0 or b1 >= lengthVar or
                a2 < 0 or a2 >= lengthVar or b2 < 0 or b2 >= lengthVar or
                a3 < 0 or a3 >= lengthVar or b3 < 0 or b3 >= lengthVar
            ):
                return float('-inf')

            # Terminal condition: all three positions converged to bottom-right corner
            if a1 == b1 == a2 == b2 == a3 == b3 == lengthVar - 1:
                return fruits[lengthVar - 1][lengthVar - 1]

            keyTuple = (a1, b1, a2, b2, a3, b3)
            if keyTuple in cacheMap:
                return cacheMap[keyTuple]

            sumCollected = fruits[a1][b1]
            # Special rules for overlapping positions:
            if (a1 == a2 and b1 == b2) or (a1 == a3 and b1 == b3):
                sumCollected = 0

            if a2 == a3 and b2 == b3:
                sumCollected += fruits[a2][b2]
            else:
                sumCollected += fruits[a2][b2] + fruits[a3][b3]

            maxValue = float('-inf')
            for dxA, dyA in vectorSetA:
                for dxB, dyB in vectorSetB:
                    for dxC, dyC in vectorSetC:
                        candidate = recursiveSearch(
                            a1 + dxA, b1 + dyA,
                            a2 + dxB, b2 + dyB,
                            a3 + dxC, b3 + dyC
                        )
                        if candidate > maxValue:
                            maxValue = candidate

            cacheMap[keyTuple] = sumCollected + maxValue
            return cacheMap[keyTuple]

        return recursiveSearch(0, 0, 0, lengthVar - 1, lengthVar - 1, 0)