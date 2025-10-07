class Solution:
    def maxOperations(self, nums):
        def dfs(a, b, c, d):
            def equalsSum(x, y, val):
                return x + y == val

            if a >= b:
                return 0

            if (a, b, c) in d:
                return d[(a, b, c)]

            z = 0

            if equalsSum(nums[a], nums[a + 1], c):
                temp1 = dfs(a + 2, b, c, d) + 1
                if temp1 > z:
                    z = temp1

            if equalsSum(nums[b], nums[b - 1], c):
                temp2 = dfs(a, b - 2, c, d) + 1
                if temp2 > z:
                    z = temp2

            if equalsSum(nums[a], nums[b], c):
                temp3 = dfs(a + 1, b - 1, c, d) + 1
                if temp3 > z:
                    z = temp3

            d[(a, b, c)] = z
            return z

        v1 = dfs(2, len(nums) - 1, nums[0] + nums[1], {}) + 1
        v2 = dfs(0, len(nums) - 3, nums[-2] + nums[-1], {}) + 1
        v3 = dfs(1, len(nums) - 2, nums[0] + nums[-1], {}) + 1

        if v1 > v2:
            return v1 if v1 > v3 else v3
        else:
            return v2 if v2 > v3 else v3