class Solution:
    def maximumTotalCost(self, nums):
        length = len(nums)
        if length == 1:
            return nums[0]

        dp = [0] * length
        dp[length - 1] = nums[length - 1]

        for index in range(length - 2, -1, -1):
            sum_ = nums[index]
            if sum_ > dp[index + 1]:
                dp[index] = sum_
            else:
                dp[index] = dp[index + 1] + sum_

            for pos in range(index + 1, length):
                sign = -1 if (pos - index) % 2 == 1 else 1
                sum_ += nums[pos] * sign

                if pos + 1 < length:
                    candidate = sum_ + dp[pos + 1]
                    if dp[index] < candidate:
                        dp[index] = candidate
                else:
                    if dp[index] < sum_:
                        dp[index] = sum_

        return dp[0]