class Solution:
    def findPermutation(self, nums):
        n = len(nums)
        limit = (1 << n) - 1
        memo = {}

        def dfs(mask, val):
            if mask == limit:
                return abs(val - nums[0])
            if (mask, val) in memo:
                return memo[(mask, val)]

            minimum = float('inf')
            for i in range(n):
                if ((mask >> i) & 1) == 0:
                    nextMask = mask | (1 << i)
                    attempt = abs(val - nums[i]) + dfs(nextMask, i)
                    if attempt < minimum:
                        minimum = attempt
            memo[(mask, val)] = minimum
            return minimum

        ans = []

        def g(mask, position):
            ans.append(position)
            if mask == limit:
                return

            target = dfs(mask, position)
            for i in range(n):
                if ((mask >> i) & 1) == 0:
                    tempVal = abs(position - nums[i]) + dfs(mask | (1 << i), i)
                    if tempVal == target:
                        g(mask | (1 << i), i)
                        break

        startMask = 1 << 0
        g(startMask, 0)
        return ans