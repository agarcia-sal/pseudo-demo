class Solution:
    def valueAfterKSeconds(self, n: int, k: int) -> int:
        LIMIT = 10**10 + 7
        buffer = [1] * n
        outerCounter = 0
        while outerCounter < k:
            innerCounter = 1
            while innerCounter < n:
                tempVal = buffer[innerCounter] + buffer[innerCounter - 1]
                calcVal = tempVal - (tempVal // LIMIT) * LIMIT
                buffer[innerCounter] = calcVal
                innerCounter += 1
            outerCounter += 1
        return buffer[n - 1]