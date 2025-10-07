from typing import List

class Solution:
    def minLargest(self, nums1: List[int], nums2: List[int]) -> int:
        def nxt(x: int, y: int) -> int:
            p = x & (1 ^ y)
            if p != 0:
                p = x + 1
            else:
                p = x + 2
            return p

        a_len = len(nums1)
        b_len = len(nums2)
        g = [[0] * (b_len + 1) for _ in range(a_len + 1)]

        # Initialize first column
        for i in range(1, a_len + 1):
            u = nums1[i - 1]
            g[i][0] = nxt(g[i - 1][0], u)

        # Initialize first row
        for j in range(1, b_len + 1):
            v = nums2[j - 1]
            g[0][j] = nxt(g[0][j - 1], v)

        # Fill the rest of the DP table
        for i in range(1, a_len + 1):
            u = nums1[i - 1]
            for j in range(1, b_len + 1):
                v = nums2[j - 1]
                temp1 = nxt(g[i - 1][j], u)
                temp2 = nxt(g[i][j - 1], v)
                g[i][j] = temp1 if temp1 < temp2 else temp2

        return g[a_len][b_len]