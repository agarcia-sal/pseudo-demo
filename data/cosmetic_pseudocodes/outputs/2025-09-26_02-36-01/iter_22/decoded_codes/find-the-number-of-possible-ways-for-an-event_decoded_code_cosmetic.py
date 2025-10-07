class Solution:
    def numberOfWays(self, n: int, x: int, y: int) -> int:
        CONST_MOD = 10**10 + 7
        matrixF = [[0] * (x + 1) for _ in range(n + 1)]
        matrixF[0][0] = 1

        for counterI in range(1, n + 1):
            for counterJ in range(1, x + 1):
                prevI = counterI - 1
                val1 = matrixF[prevI][counterJ] * counterJ
                val2 = matrixF[prevI][counterJ - 1] * (x - (counterJ - 1))
                matrixF[counterI][counterJ] = (val1 + val2) % CONST_MOD

        totalAns = 0
        powerVal = 1
        for counterK in range(1, x + 1):
            powerVal = (powerVal * y) % CONST_MOD
            addVal = (matrixF[n][counterK] * powerVal) % CONST_MOD
            totalAns = (totalAns + addVal) % CONST_MOD

        return totalAns