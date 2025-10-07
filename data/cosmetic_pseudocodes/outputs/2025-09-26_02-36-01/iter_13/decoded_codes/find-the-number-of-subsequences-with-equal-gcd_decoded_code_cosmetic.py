class Solution:
    def subsequencePairCount(self, nums):
        MODULO = 5 * (10 ** 8) + 2 * (10 ** 8) + 7

        def computeGCD(a, b):
            while b != 0:
                a, b = b, a % b
            return a

        def zeroMatrix(rows, cols):
            return [[0] * cols for _ in range(rows)]

        maxValue = 0
        for num in nums:
            if num > maxValue:
                maxValue = num

        dynamic = zeroMatrix(maxValue + 1, maxValue + 1)
        dynamic[0][0] = 1

        for num in nums:
            intermediate = zeroMatrix(maxValue + 1, maxValue + 1)

            def innerLoopX(x, y):
                intermediate[x][y] = (intermediate[x][y] + dynamic[x][y]) % MODULO

                vX = computeGCD(x, num)
                intermediate[vX][y] = (intermediate[vX][y] + dynamic[x][y]) % MODULO

                vY = computeGCD(y, num)
                intermediate[x][vY] = (intermediate[x][vY] + dynamic[x][y]) % MODULO

            def loopY(x, y):
                if y > maxValue:
                    return
                innerLoopX(x, y)
                loopY(x, y + 1)

            def loopX(x):
                if x > maxValue:
                    return
                loopY(x, 0)
                loopX(x + 1)

            loopX(0)
            dynamic = intermediate

        total = 0

        def addG(g):
            nonlocal total
            if g > maxValue:
                return
            total = (total + dynamic[g][g]) % MODULO
            addG(g + 1)

        addG(1)
        return total