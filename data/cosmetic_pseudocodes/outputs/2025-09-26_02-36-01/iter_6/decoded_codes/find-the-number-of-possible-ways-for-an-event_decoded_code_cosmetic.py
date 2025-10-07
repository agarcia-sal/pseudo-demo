class Solution:
    def numberOfWays(self, m: int, a: int, b: int) -> int:
        modulo = 10**10 + 7

        def remainderSumProduct(u: int, v: int, w: int) -> int:
            return (u + v) % w

        def remainderProduct(u: int, v: int, w: int) -> int:
            return (u * v) % w

        g = []
        for _ in range(m + 1):
            g.append([0] * (a + 1))
        g[0][0] = 1

        for indexX in range(1, m + 1):
            for indexY in range(1, a + 1):
                prevOne = g[indexX - 1][indexY]
                prevTwo = g[indexX - 1][indexY - 1]
                partOne = remainderProduct(prevOne, indexY, modulo)
                diffVal = a - (indexY + (1 - 2))  # simplifies to a - indexY + 1
                partTwo = remainderProduct(prevTwo, diffVal, modulo)
                combined = remainderSumProduct(partOne, partTwo, modulo)
                g[indexX][indexY] = combined

        resultAccumulator = 0
        powerVal = 1
        for iteratorZ in range(1, a + 1):
            powerVal = (powerVal * b) % modulo
            tempVal = (g[m][iteratorZ] * powerVal) % modulo
            resultAccumulator = (resultAccumulator + tempVal) % modulo

        return resultAccumulator