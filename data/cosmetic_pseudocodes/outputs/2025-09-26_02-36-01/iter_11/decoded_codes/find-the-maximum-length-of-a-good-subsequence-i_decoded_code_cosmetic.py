class Solution:
    def maximumLength(self, nums, k):
        m = len(nums)
        dp = [[1] * (k + 1) for _ in range(m)]
        result = 0
        p = m - 1
        while p >= 0:
            q = 0
            while q <= k:
                r = 0
                while r < p:
                    if nums[p] == nums[r]:
                        dp[p][q] = max(dp[p][q], dp[r][q] + 1)
                    else:
                        if q > 0:
                            tempVal = dp[r][q - 1] + 1
                            dp[p][q] = max(dp[p][q], tempVal)
                    r += 1
                q += 1
            if dp[p][k] > result:
                result = dp[p][k]
            p -= 1
        return result