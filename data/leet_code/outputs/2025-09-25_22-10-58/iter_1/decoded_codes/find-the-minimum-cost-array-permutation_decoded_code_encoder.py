class Solution:
    def findPermutation(self, nums):
        n = len(nums)
        ans = []

        def dfs(mask, pre):
            if mask == (1 << n) - 1:
                return abs(pre - nums[0])

            res = float('inf')
            for cur in range(n):
                if ((mask >> cur) & 1) == 0:
                    candidate_value = abs(pre - nums[cur]) + dfs(mask | (1 << cur), cur)
                    if candidate_value < res:
                        res = candidate_value
            return res

        def g(mask, pre):
            ans.append(pre)
            if mask == (1 << n) - 1:
                return

            res = dfs(mask, pre)
            for cur in range(n):
                if ((mask >> cur) & 1) == 0:
                    candidate_value = abs(pre - nums[cur]) + dfs(mask | (1 << cur), cur)
                    if candidate_value == res:
                        g(mask | (1 << cur), cur)
                        break

        g(1 << 0, 0)
        return ans