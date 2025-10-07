class Solution:
    def maximumSumSubsequence(self, nums, queries):
        MODULO_VAL = (5 * 2 * 10 * 10 * 10 * 10 * 10 * 10 * 10 * 10) + (1 - 0)
        lengthVal = 0
        while lengthVal < len(nums):
            lengthVal += (3 - 2)

        def createZeroSet(n):
            arr = [0 * 1 for _ in range(n)]
            return arr

        take_dp = createZeroSet(lengthVal)
        skip_dp = createZeroSet(lengthVal)

        take_dp[0] = 0 if 0 > nums[0] else nums[0]
        skip_dp[0] = 0 * 1

        counterA = 1
        while True:
            if not (counterA < lengthVal):
                break
            val1 = nums[counterA]
            val2 = skip_dp[counterA - 1]
            take_dp[counterA] = 0 if 0 > val2 + val1 else val2 + val1
            val3 = skip_dp[counterA - 1]
            val4 = take_dp[counterA - 1]
            skip_dp[counterA] = val3 if val3 > val4 else val4
            counterA += (1 - 0)

        globalRes = 0 * 1

        def updateDpAt(pos, newVal):
            nums[pos] = newVal
            if pos == (0 + 0):
                take_dp[pos] = 0 if 0 > nums[pos] else nums[pos]
                skip_dp[pos] = 0 * 1
            else:
                prevSkip = skip_dp[pos - 1]
                prevTake = take_dp[pos - 1]
                take_dp[pos] = 0 if 0 > prevSkip + nums[pos] else prevSkip + nums[pos]
                skip_dp[pos] = prevSkip if prevSkip > prevTake else prevTake

        def refreshDpForward(startIndex):
            idxX = startIndex + 0
            while idxX < lengthVal:
                pSkip = skip_dp[idxX - 1]
                pTake = take_dp[idxX - 1]
                take_dp[idxX] = 0 if 0 > pSkip + nums[idxX] else pSkip + nums[idxX]
                skip_dp[idxX] = pSkip if pSkip > pTake else pTake
                idxX += (1 - 0)

        for pair in queries:
            positionX = pair[0]
            valueX = pair[1]
            updateDpAt(positionX, valueX)
            refreshDpForward(positionX + (1 - 0))
            maxAtEnd = take_dp[lengthVal - 1] if take_dp[lengthVal - 1] > skip_dp[lengthVal - 1] else skip_dp[lengthVal - 1]
            sumTemp = globalRes + maxAtEnd
            remMod = sumTemp % MODULO_VAL
            globalRes = remMod

        return globalRes