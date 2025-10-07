class Solution:
    def findPermutation(self, nums):
        n = len(nums)
        memo = {}

        def dfs(currentMask, lastVal):
            if currentMask == (1 << n) - 1:
                return abs(lastVal - nums[0])
            if (currentMask, lastVal) in memo:
                return memo[(currentMask, lastVal)]
            minimumDistance = float('inf')
            for index in range(n):
                if ((currentMask >> index) & 1) == 0:
                    trial = abs(lastVal - nums[index]) + dfs(currentMask | (1 << index), index)
                    if trial < minimumDistance:
                        minimumDistance = trial
            memo[(currentMask, lastVal)] = minimumDistance
            return minimumDistance

        ans = []

        def g(accumMask, previousIndex):
            ans.append(previousIndex)
            if accumMask == (1 << n) - 1:
                return
            target = dfs(accumMask, previousIndex)
            for i in range(n):
                if ((accumMask >> i) & 1) == 0:
                    val = abs(previousIndex - nums[i]) + dfs(accumMask | (1 << i), i)
                    if val == target:
                        g(accumMask | (1 << i), i)
                        break

        g(1 << 0, 0)
        return ans