class Solution:
    def maximumTotalCost(self, nums):
        def PowNeg(e):
            # Returns (-1)^e using recursion
            if e == 0:
                return 1
            elif e % 2 == 0:
                return -PowNeg(e - 1)
            else:
                return PowNeg(e - 1)

        def EvaluateInner(cidx, jdx, ccost, n, dp, nums):
            if jdx >= n:
                return
            signVal = PowNeg(jdx - cidx)
            ccost += nums[jdx] * signVal
            if jdx + 1 < n:
                if dp[cidx] < ccost + dp[jdx + 1]:
                    dp[cidx] = ccost + dp[jdx + 1]
            else:
                if dp[cidx] < ccost:
                    dp[cidx] = ccost
            EvaluateInner(cidx, jdx + 1, ccost, n, dp, nums)

        def WalkC(i, n, dp, nums):
            if i < 0:
                return

            curc = nums[i]
            if curc > dp[i + 1]:
                dp[i] = curc
            else:
                dp[i] = dp[i + 1] + curc
            EvaluateInner(i, i + 1, curc, n, dp, nums)
            WalkC(i - 1, n, dp, nums)

        length = len(nums)
        if length == 1:
            return nums[0]

        dp = [0] * length
        dp[length - 1] = nums[length - 1]
        WalkC(length - 2, length, dp, nums)

        return dp[0]