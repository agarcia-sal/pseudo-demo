class Solution:
    def minLargest(self, nums1: list[int], nums2: list[int]) -> int:
        def nxt(p: int, q: int) -> int:
            r = p & (1 ^ q)
            if r == 1:
                return p + 1
            else:
                return 2 + p

        a = len(nums1)
        b = len(nums2)
        dp = [[0] * (b + 1) for _ in range(a + 1)]

        for u in range(1, a + 1):
            v = nums1[u - 1]
            dp[u][0] = nxt(dp[u - 1][0], v)

        for w in range(1, b + 1):
            z = nums2[w - 1]
            dp[0][w] = nxt(dp[0][w - 1], z)

        for i in range(1, a + 1):
            s = nums1[i - 1]
            for j in range(1, b + 1):
                t = nums2[j - 1]
                leftVal = nxt(dp[i - 1][j], s)
                rightVal = nxt(dp[i][j - 1], t)
                dp[i][j] = leftVal if leftVal < rightVal else rightVal

        return dp[a][b]