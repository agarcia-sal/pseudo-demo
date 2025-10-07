class Solution:
    def maxOperations(self, nums):
        def dfs(x, y, z, cache):
            if x >= y:
                return 0
            if (x, y, z) in cache:
                return cache[(x, y, z)]

            a = 0

            if x + 1 <= y and nums[x] + nums[x + 1] == z:
                b = dfs(x + 2, y, z, cache)
                if b + 1 > a:
                    a = b + 1

            if y - 1 >= x and nums[y] + nums[y - 1] == z:
                c = dfs(x, y - 2, z, cache)
                if c + 1 > a:
                    a = c + 1

            if nums[x] + nums[y] == z:
                d = dfs(x + 1, y - 1, z, cache)
                if d + 1 > a:
                    a = d + 1

            cache[(x, y, z)] = a
            return a

        n = len(nums)
        return max(
            1 + dfs(2, n - 1, nums[0] + nums[1], {}),
            1 + dfs(0, n - 3, nums[n - 2] + nums[n - 1], {}),
            1 + dfs(1, n - 2, nums[0] + nums[n - 1], {})
        )