class Solution:
    def numberOfWays(self, n: int, x: int, y: int) -> int:
        moduloValue = 10**9 + 7

        dp = [[0] * (x + 1) for _ in range(n + 1)]
        dp[0][0] = 1

        outerIndex = 1
        while outerIndex <= n:
            innerIndex = 1
            while innerIndex <= x:
                prev_i = outerIndex - 1
                prev_j = innerIndex
                prev_j_minus_one = innerIndex - 1

                leftTerm = dp[prev_i][prev_j] * prev_j if prev_j <= x else 0
                rightTermFactor = x - (innerIndex - 1) - 1
                rightTerm = dp[prev_i][prev_j_minus_one] * rightTermFactor if prev_j_minus_one >= 0 else 0

                dp[outerIndex][innerIndex] = (leftTerm + rightTerm) % moduloValue

                innerIndex += 1
            outerIndex += 1

        result = 0
        powerAcc = 1

        for index in range(1, x + 1):
            powerAcc = (powerAcc * y) % moduloValue
            tempVal = dp[n][index] * powerAcc
            result = (result + tempVal) % moduloValue

        return result