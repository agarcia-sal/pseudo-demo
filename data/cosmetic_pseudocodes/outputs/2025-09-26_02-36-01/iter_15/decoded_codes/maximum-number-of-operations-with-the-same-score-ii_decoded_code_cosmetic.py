class Solution:
    def maxOperations(self, nums):
        def dfs(a, b, c, d):
            if a >= b:
                return 0
            if (a, b, c) in d:
                return d[(a, b, c)]
            e = 0
            if nums[a] + nums[a + 1] == c:
                f = dfs(a + 2, b, c, d) + 1
                if f > e:
                    e = f
            if nums[b] + nums[b - 1] == c:
                g = dfs(a, b - 2, c, d) + 1
                if g > e:
                    e = g
            if nums[a] + nums[b] == c:
                h = dfs(a + 1, b - 1, c, d) + 1
                if h > e:
                    e = h
            d[(a, b, c)] = e
            return e

        n = len(nums)
        if n < 2:
            return 0
        j = nums[0] + nums[1]
        k = nums[n - 2] + nums[n - 1]
        m = nums[0] + nums[n - 1]

        return max(
            1 + dfs(2, n - 1, j, {}),
            1 + dfs(0, n - 3, k, {}),
            1 + dfs(1, n - 2, m, {}),
        )