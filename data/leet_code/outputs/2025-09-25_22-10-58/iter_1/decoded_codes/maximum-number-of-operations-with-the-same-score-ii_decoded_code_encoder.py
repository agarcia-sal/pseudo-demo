class Solution:
    def maxOperations(self, nums):
        def dfs(l, r, prev_score, memo):
            if l >= r:
                return 0
            key = (l, r, prev_score)
            if key in memo:
                return memo[key]
            max_ops = 0
            if l + 1 < len(nums) and nums[l] + nums[l + 1] == prev_score:
                max_ops = max(max_ops, 1 + dfs(l + 2, r, prev_score, memo))
            if r - 1 >= 0 and nums[r] + nums[r - 1] == prev_score:
                max_ops = max(max_ops, 1 + dfs(l, r - 2, prev_score, memo))
            if nums[l] + nums[r] == prev_score:
                max_ops = max(max_ops, 1 + dfs(l + 1, r - 1, prev_score, memo))
            memo[key] = max_ops
            return max_ops

        n = len(nums)
        return max(
            1 + dfs(2, n - 1, nums[0] + nums[1], {}),
            1 + dfs(0, n - 3, nums[n - 2] + nums[n - 1], {}),
            1 + dfs(1, n - 2, nums[0] + nums[n - 1], {}),
        )