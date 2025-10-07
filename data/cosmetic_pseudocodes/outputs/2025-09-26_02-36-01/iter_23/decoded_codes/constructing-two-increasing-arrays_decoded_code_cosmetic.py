class Solution:
    def minLargest(self, nums1: list[int], nums2: list[int]) -> int:
        def nxt(a: int, b: int) -> int:
            # If the least significant bit of a XOR b is 1, add 1; else add 2
            if (a & (1 ^ b)) == 1:
                return a + 1
            else:
                return a + 2

        p, q = len(nums1), len(nums2)
        table = [[0] * (q + 1) for _ in range(p + 1)]

        def fillRow(r: int):
            if r > p:
                return
            val = nums1[r - 1]
            temp = nxt(table[r - 1][0], val)
            table[r][0] = temp
            fillRow(r + 1)

        def fillCol(c: int):
            if c > q:
                return
            val = nums2[c - 1]
            temp = nxt(table[0][c - 1], val)
            table[0][c] = temp
            fillCol(c + 1)

        def fillCells(i: int, j: int):
            if i > p:
                return
            if j > q:
                fillCells(i + 1, 1)
                return
            a_val = nums1[i - 1]
            b_val = nums2[j - 1]
            v1 = nxt(table[i - 1][j], a_val)
            v2 = nxt(table[i][j - 1], b_val)
            table[i][j] = v1 if v1 < v2 else v2
            fillCells(i, j + 1)

        fillRow(1)
        fillCol(1)
        fillCells(1, 1)

        return table[p][q]