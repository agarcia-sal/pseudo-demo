class Solution:
    def maximumTotalCost(self, nums):
        n = len(nums)
        if n == 1:
            return nums[0]

        dp = [0] * n
        dp[-1] = nums[-1]

        for i in range(n - 2, -1, -1):
            current_cost = nums[i]
            if current_cost > dp[i + 1]:
                dp[i] = current_cost
            else:
                dp[i] = dp[i + 1] + current_cost

            for j in range(i + 1, n):
                alternating_sign = (-1) ** (j - i)
                current_cost += nums[j] * alternating_sign

                if j + 1 < n:
                    if dp[i] < current_cost + dp[j + 1]:
                        dp[i] = current_cost + dp[j + 1]
                else:
                    if dp[i] < current_cost:
                        dp[i] = current_cost

        return dp[0]