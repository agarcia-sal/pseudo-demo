class Solution:
    def maximumSumSubsequence(self, nums, queries):
        LIMIT = 10**9 + 1
        lengthCount = len(nums)

        takeDP = [0] * lengthCount
        skipDP = [0] * lengthCount

        takeDP[0] = nums[0] if nums[0] > 0 else 0
        skipDP[0] = 0

        for i in range(1, lengthCount):
            takeDP[i] = skipDP[i - 1] + nums[i] if skipDP[i - 1] + nums[i] > 0 else 0
            skipDP[i] = skipDP[i - 1] if skipDP[i - 1] > takeDP[i - 1] else takeDP[i - 1]

        accumulatedResult = 0

        def updateDP(startIndex):
            idx = startIndex + 1
            while idx < lengthCount:
                takeDP[idx] = skipDP[idx - 1] + nums[idx] if skipDP[idx - 1] + nums[idx] > 0 else 0
                skipDP[idx] = skipDP[idx - 1] if skipDP[idx - 1] > takeDP[idx - 1] else takeDP[idx - 1]
                idx += 1

        for position, val in queries:
            nums[position] = val
            if position == 0:
                takeDP[position] = nums[position] if nums[position] > 0 else 0
                skipDP[position] = 0
            else:
                takeDP[position] = skipDP[position - 1] + nums[position] if skipDP[position - 1] + nums[position] > 0 else 0
                skipDP[position] = skipDP[position - 1] if skipDP[position - 1] > takeDP[position - 1] else takeDP[position - 1]

            updateDP(position)

            maxEndVal = takeDP[-1] if takeDP[-1] > skipDP[-1] else skipDP[-1]
            accumulatedResult = (accumulatedResult + maxEndVal) % LIMIT

        return accumulatedResult