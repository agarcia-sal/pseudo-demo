class Solution:
    def minLargest(self, nums1: list[int], nums2: list[int]) -> int:

        def nxt(x: int, y: int) -> int:
            if ((x & 1) ^ y) == 1:
                return x + 1
            else:
                return x + 2

        def fillRow(i: int, f: list[list[int]], l: list[int]) -> None:
            if i > len(l):
                return
            f[i][0] = nxt(f[i - 1][0], l[i - 1])
            fillRow(i + 1, f, l)

        def fillColumn(j: int, f: list[list[int]], l: list[int]) -> None:
            if j > len(l):
                return
            f[0][j] = nxt(f[0][j - 1], l[j - 1])
            fillColumn(j + 1, f, l)

        def fillGrid(i: int, j: int, m: int, n: int, f: list[list[int]], l1: list[int], l2: list[int]) -> None:
            if i > m:
                return
            if j > n:
                fillGrid(i + 1, 1, m, n, f, l1, l2)
                return
            a = nxt(f[i - 1][j], l1[i - 1])
            b = nxt(f[i][j - 1], l2[j - 1])
            f[i][j] = a if a < b else b
            fillGrid(i, j + 1, m, n, f, l1, l2)

        m = len(nums1)
        n = len(nums2)
        f = [[0] * (n + 1) for _ in range(m + 1)]

        fillRow(1, f, nums1)
        fillColumn(1, f, nums2)
        fillGrid(1, 1, m, n, f, nums1, nums2)

        return f[m][n]