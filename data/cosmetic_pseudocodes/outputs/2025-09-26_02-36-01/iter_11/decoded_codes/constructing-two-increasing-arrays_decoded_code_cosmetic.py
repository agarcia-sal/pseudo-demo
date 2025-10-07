class Solution:
    def minLargest(self, nums1: list[int], nums2: list[int]) -> int:
        def nxt(a: int, b: int) -> int:
            # If (a & 1) XOR b is 1, add 1 to a; else add 2
            if ((a & 1) ^ b) == 1:
                return a + 1
            else:
                return a + 2

        p = len(nums1)
        q = len(nums2)
        # dp dimensions: (p+1) x (q+1)
        dp = [[0] * (q + 1) for _ in range(p + 1)]

        # Convert 1-based indexing as per pseudocode by adjusting indexing
        # Here nums1[u] corresponds to nums1[u-1] in Python's 0-based indexing
        for u in range(1, p + 1):
            val = nums1[u - 1]
            dp[u][0] = nxt(dp[u - 1][0], val)

        for v in range(1, q + 1):
            val2 = nums2[v - 1]
            dp[0][v] = nxt(dp[0][v - 1], val2)

        def minOfTwo(x: int, y: int) -> int:
            return x if x < y else y

        for i_outer in range(1, p + 1):
            xx = nums1[i_outer - 1]
            for j_inner in range(1, q + 1):
                yy = nums2[j_inner - 1]
                option1 = nxt(dp[i_outer - 1][j_inner], xx)
                option2 = nxt(dp[i_outer][j_inner - 1], yy)
                dp[i_outer][j_inner] = minOfTwo(option1, option2)

        return dp[p][q]