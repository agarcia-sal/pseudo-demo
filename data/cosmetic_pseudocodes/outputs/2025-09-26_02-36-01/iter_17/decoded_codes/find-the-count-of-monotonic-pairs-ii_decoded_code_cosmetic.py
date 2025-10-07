class Solution:
    def countOfPairs(self, nums):
        M = 10**9 + 7
        l = len(nums)
        h = nums[0]
        dp = [[[0] * (h + 1) for _ in range(h + 1)] for _ in range(l + 1)]

        for y in range(h + 1):
            dp[1][y][h - y] = 1

        for x in range(2, l + 1):
            h = nums[x - 1]
            for y in range(h + 1):
                for z in range(h + 1):
                    if y + z == h:
                        for f in range(y + 1):
                            for r in range(z, len(dp[0][0])):
                                dp[x][y][z] = (dp[x][y][z] + dp[x - 1][f][r]) % M

        r = 0
        length = len(dp[0])
        for y in range(length):
            for z in range(length):
                r = (r + dp[l][y][z]) % M

        return r