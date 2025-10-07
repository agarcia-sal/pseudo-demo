class Solution:
    def maximumSumSubsequence(self, nums, queries):
        MOD = 10**9 + 1
        n = len(nums)
        dp_take = [0] * n
        dp_skip = [0] * n

        dp_take[0] = max(0, nums[0])
        dp_skip[0] = 0

        for i in range(1, n):
            dp_take[i] = max(0, dp_skip[i - 1]) + nums[i]
            dp_skip[i] = max(dp_skip[i - 1], dp_take[i - 1])

        total_result = 0
        for pos, x in queries:
            nums[pos] = x
            if pos == 0:
                dp_take[pos] = max(0, nums[pos])
                dp_skip[pos] = 0
            else:
                dp_take[pos] = max(0, dp_skip[pos - 1]) + nums[pos]
                dp_skip[pos] = max(dp_skip[pos - 1], dp_take[pos - 1])
            for i in range(pos + 1, n):
                dp_take[i] = max(0, dp_skip[i - 1]) + nums[i]
                dp_skip[i] = max(dp_skip[i - 1], dp_take[i - 1])
            total_result = (total_result + max(dp_take[-1], dp_skip[-1])) % MOD

        return total_result