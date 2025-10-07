class Solution:
    def minLargest(self, nums1: list[int], nums2: list[int]) -> int:
        def nxt(x: int, y: int) -> int:
            # if (x & (1 ^ y)) == 1, return x + 1 else x + 2
            # note: 1 ^ y means 1 XOR y
            if (x & (1 ^ y)) == 1:
                return x + 1
            else:
                return x + 2

        m, n = len(nums1), len(nums2)
        f = [[0] * (n + 1) for _ in range(m + 1)]

        for i in range(1, m + 1):
            x = nums1[i - 1]
            f[i][0] = nxt(f[i - 1][0], x)

        for j in range(1, n + 1):
            y = nums2[j - 1]
            f[0][j] = nxt(f[0][j - 1], y)

        for i in range(1, m + 1):
            x = nums1[i - 1]
            for j in range(1, n + 1):
                y = nums2[j - 1]
                f[i][j] = min(nxt(f[i - 1][j], x), nxt(f[i][j - 1], y))

        return f[m][n]