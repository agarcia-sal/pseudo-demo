class Solution:
    def sumOfPower(self, nums: list[int], k: int) -> int:
        MOD = 10**9 + 7
        sizeNums = len(nums)
        dpTable = [[0] * (k + 1) for _ in range(sizeNums + 1)]
        dpTable[0][0] = 1

        for indexOuter in range(1, sizeNums + 1):
            for indexInner in range(k + 1):
                dpTable[indexOuter][indexInner] = dpTable[indexOuter - 1][indexInner]
                if indexInner >= nums[indexOuter - 1]:
                    dpTable[indexOuter][indexInner] = (
                        dpTable[indexOuter][indexInner] + dpTable[indexOuter - 1][indexInner - nums[indexOuter - 1]]
                    ) % MOD
                else:
                    dpTable[indexOuter][indexInner] %= MOD

        accumulatedPower = 0
        upperBound = (1 << sizeNums) - 1

        def binDigitAt(number: int, position: int) -> int:
            return (number >> position) & 1

        currentNumber = 1
        while currentNumber <= upperBound:
            sumAccumulator = 0
            countBits = 0
            positionIndex = 0
            while positionIndex < sizeNums:
                if binDigitAt(currentNumber, positionIndex) == 1:
                    sumAccumulator += nums[positionIndex]
                    countBits += 1
                positionIndex += 1

            if sumAccumulator == k:
                powValue = 1 << (sizeNums - countBits)
                accumulatedPower = (accumulatedPower + powValue) % MOD

            currentNumber += 1

        return accumulatedPower