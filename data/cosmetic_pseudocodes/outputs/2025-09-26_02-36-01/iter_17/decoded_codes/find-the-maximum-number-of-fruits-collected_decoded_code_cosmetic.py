class Solution:
    def maxCollectedFruits(self, fruits):
        totalLength = len(fruits)

        shiftsA = [(1, 1), (0, 1)]
        shiftsB = [(1, 0), (1, -1), (1, 1)]
        shiftsC = [(-1, 1), (0, 1), (1, 1)]

        cache = {}

        def dp(a1, b1, a2, b2, a3, b3):
            # Check boundaries
            if (
                a1 < 0 or a1 >= totalLength or b1 < 0 or b1 >= totalLength or
                a2 < 0 or a2 >= totalLength or b2 < 0 or b2 >= totalLength or
                a3 < 0 or a3 >= totalLength or b3 < 0 or b3 >= totalLength
            ):
                return float('-inf')

            # Check goal position
            if a1 == b1 == a2 == b2 == a3 == b3 == totalLength - 1:
                return fruits[totalLength - 1][totalLength - 1]

            keyTuple = (a1, b1, a2, b2, a3, b3)
            if keyTuple in cache:
                return cache[keyTuple]

            val1 = fruits[b1][a1]
            val2 = fruits[b2][a2]
            val3 = fruits[b3][a3]

            sumCollected = val1
            if (a1 == a2 and b1 == b2) or (a1 == a3 and b1 == b3):
                sumCollected += 0
            else:
                sumCollected += val2

            if a2 == a3 and b2 == b3:
                sumCollected += 0
            else:
                sumCollected += val3

            currentMax = float('-inf')

            for stepA, stepB in shiftsA:
                for stepC, stepD in shiftsB:
                    for stepE, stepF in shiftsC:
                        nextVal = dp(a1 + stepA, b1 + stepB, a2 + stepC, b2 + stepD, a3 + stepE, b3 + stepF)
                        if nextVal > currentMax:
                            currentMax = nextVal

            cache[keyTuple] = sumCollected + currentMax
            return cache[keyTuple]

        return dp(0, 0, 0, totalLength - 1, totalLength - 1, 0)