class Solution:
    def maxOperations(self, nums):
        def dfs(alpha, beta, gamma, delta):
            if alpha >= beta:
                return 0
            key = (alpha, beta, gamma)
            if key in delta:
                return delta[key]

            sigma = 0
            if nums[alpha] + nums[alpha + 1] == gamma:
                sigma = max(sigma, 1 + dfs(alpha + 2, beta, gamma, delta))
            if nums[beta] + nums[beta - 1] == gamma:
                sigma = max(sigma, 1 + dfs(alpha, beta - 2, gamma, delta))
            if nums[alpha] + nums[beta] == gamma:
                sigma = max(sigma, 1 + dfs(alpha + 1, beta - 1, gamma, delta))

            delta[key] = sigma
            return sigma

        n = len(nums)
        result1 = 1 + dfs(2, n - 1, nums[0] + nums[1], {})
        result2 = 1 + dfs(0, n - 3, nums[n - 2] + nums[n - 1], {})
        result3 = 1 + dfs(1, n - 2, nums[0] + nums[n - 1], {})

        return max(result1, result2, result3)