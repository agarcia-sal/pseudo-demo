from typing import List

class Solution:
    def minLargest(self, nums1: List[int], nums2: List[int]) -> int:
        def nxt(x: int, y: int) -> int:
            if (x & (1 ^ y)) == 1:
                return x + 1
            else:
                return x + 2

        m, n = len(nums1), len(nums2)
        f = [[0] * (n + 1) for _ in range(m + 1)]

        for i in range(1, m + 1):
            current_x = nums1[i - 1]
            prev_val = f[i - 1][0]
            f[i][0] = nxt(prev_val, current_x)

        for j in range(1, n + 1):
            current_y = nums2[j - 1]
            prev_val = f[0][j - 1]
            f[0][j] = nxt(prev_val, current_y)

        for i in range(1, m + 1):
            current_x = nums1[i - 1]
            for j in range(1, n + 1):
                current_y = nums2[j - 1]
                option1 = nxt(f[i - 1][j], current_x)
                option2 = nxt(f[i][j - 1], current_y)
                f[i][j] = min(option1, option2)

        return f[m][n]