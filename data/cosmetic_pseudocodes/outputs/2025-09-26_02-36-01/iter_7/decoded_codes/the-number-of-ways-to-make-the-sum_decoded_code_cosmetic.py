class Solution:
    def numberOfWays(self, n: int) -> int:
        modValue = 1_000_000_007
        tallyList = [0] * (n + 1)
        tallyList[0] = 1
        denominationArray = [1, 2, 6]

        for currentDenominator in denominationArray:
            innerCounter = currentDenominator
            while innerCounter <= n:
                tallyList[innerCounter] = (tallyList[innerCounter] + tallyList[innerCounter - currentDenominator]) % modValue
                innerCounter += 1

        accumulator = 0
        loopCount = 0
        while loopCount <= 2:
            if (loopCount * 4) <= n:
                accumulator = (accumulator + tallyList[n - (loopCount * 4)]) % modValue
            loopCount += 1

        return accumulator