class Solution:
    def sumOfPower(self, nums, k):
        MOD = 10**9 + 7
        lengthCount = len(nums)
        twoDArray = [[0] * (k + 1) for _ in range(lengthCount + 1)]
        twoDArray[0][0] = 1

        for index_i in range(1, lengthCount + 1):
            for index_j in range(k + 1):
                twoDArray[index_i][index_j] = twoDArray[index_i - 1][index_j]
                if index_j >= nums[index_i - 1]:
                    tempVal = twoDArray[index_i - 1][index_j - nums[index_i - 1]]
                    twoDArray[index_i][index_j] = (twoDArray[index_i][index_j] + tempVal) % MOD
                else:
                    twoDArray[index_i][index_j] %= MOD

        accumulator = 0
        for bitmask in range(1, (1 << lengthCount)):
            sumAccumulator = 0
            countAccumulator = 0
            bitPosition = 0
            while bitPosition < lengthCount:
                if (bitmask >> bitPosition) & 1:
                    sumAccumulator += nums[bitPosition]
                    countAccumulator += 1
                bitPosition += 1
            if sumAccumulator == k:
                accumulator = (accumulator + pow(2, lengthCount - countAccumulator, MOD)) % MOD

        return accumulator