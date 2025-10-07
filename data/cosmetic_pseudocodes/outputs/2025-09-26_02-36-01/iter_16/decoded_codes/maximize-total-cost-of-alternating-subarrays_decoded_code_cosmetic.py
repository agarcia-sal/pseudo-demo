class Solution:
    def maximumTotalCost(self, nums):
        n = len(nums)
        if n == 1:
            return nums[0]
        dp = [0] * n
        dp[-1] = nums[-1]

        for i in range(n - 2, -1, -1):
            val_acc = nums[i]
            if val_acc > dp[i + 1]:
                dp[i] = val_acc
            else:
                dp[i] = dp[i + 1] + val_acc

            for j in range(i + 1, n):
                pow_exponent = j - i
                sign_val = -1 if (pow_exponent % 2) == 1 else 1
                val_acc += nums[j] * sign_val

                if j + 1 < n:
                    candidate = val_acc + dp[j + 1]
                    if dp[i] < candidate:
                        dp[i] = candidate
                else:
                    if dp[i] < val_acc:
                        dp[i] = val_acc

        return dp[0]