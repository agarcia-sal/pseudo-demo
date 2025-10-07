class Solution:
    def sumOfPower(self, nums: list[int], k: int) -> int:
        M = 10**9 + 7
        u = len(nums)
        dp = [[0] * (k + 1) for _ in range(u + 1)]
        dp[0][0] = 1

        for idx in range(1, u + 1):
            num = nums[idx - 1]
            for p in range(k + 1):
                dp[idx][p] = dp[idx - 1][p]
                if p >= num:
                    dp[idx][p] += dp[idx - 1][p - num]
                dp[idx][p] %= M

        totalPowerSum = 0
        limit = (1 << u) - 1

        def countBitsAndSum(x: int) -> tuple[int, int]:
            sVal = 0
            bCount = 0
            bitPos = 0
            while bitPos < u:
                if (x >> bitPos) & 1 == 1:
                    sVal += nums[bitPos]
                    bCount += 1
                bitPos += 1
            return sVal, bCount

        current = 1
        while current <= limit:
            accSum, cnt = countBitsAndSum(current)
            if accSum == k:
                totalPowerSum = (totalPowerSum + pow(2, u - cnt, M)) % M
            current += 1

        return totalPowerSum