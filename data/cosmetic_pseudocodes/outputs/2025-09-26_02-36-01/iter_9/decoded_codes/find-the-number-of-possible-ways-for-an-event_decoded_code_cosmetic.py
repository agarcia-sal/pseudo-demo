class Solution:
    def numberOfWays(self, q: int, r: int, s: int) -> int:
        modulus = 10**9 + 7

        def modAdd(a: int, b: int, m: int) -> int:
            res = a + b
            if res >= m:
                res -= m
            return res

        def modMul(a: int, b: int, m: int) -> int:
            return (a * b) % m

        def initializeMatrix(rows: int, cols: int) -> list[list[int]]:
            return [[0]*cols for _ in range(rows)]

        W = initializeMatrix(q + 1, r + 1)
        W[0][0] = 1

        def computeValue(i: int, j: int) -> int:
            prior_i = i - 1
            part1 = modMul(W[prior_i][j], j, modulus) if j <= r else 0
            part2 = modMul(W[prior_i][j - 1], (r - j + 1), modulus) if j - 1 >= 0 else 0
            return (part1 + part2) % modulus

        for rowCounter in range(1, q + 1):
            for colCounter in range(1, r + 1):
                W[rowCounter][colCounter] = computeValue(rowCounter, colCounter)

        total = 0
        powerAcc = 1
        for indexCounter in range(1, r + 1):
            powerAcc = (powerAcc * s) % modulus
            total = (total + (W[q][indexCounter] * powerAcc) % modulus) % modulus

        return total