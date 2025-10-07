class Solution:
    def maxOperations(self, nums):
        def dfs(a, b, x, cache):
            if a >= b:
                return 0
            if (a, b, x) in cache:
                return cache[(a, b, x)]
            result = 0
            if nums[a] + nums[a + 1] == x:
                result = max(result, 1 + dfs(a + 2, b, x, cache))
            if nums[b] + nums[b - 1] == x:
                result = max(result, 1 + dfs(a, b - 2, x, cache))
            if nums[a] + nums[b] == x:
                result = max(result, 1 + dfs(a + 1, b - 1, x, cache))
            cache[(a, b, x)] = result
            return result

        p = 1 + dfs(2, len(nums) - 1, nums[0] + nums[1], {})
        q = 1 + dfs(0, len(nums) - 3, nums[len(nums) - 2] + nums[len(nums) - 1], {})
        r = 1 + dfs(1, len(nums) - 2, nums[0] + nums[len(nums) - 1], {})
        return max(p, q, r)