class Solution:
    def minLargest(self, nums1: list[int], nums2: list[int]) -> int:
        def nxt(a: int, b: int) -> int:
            # Increment a by 1 or 2 depending on parity condition
            if ((a & 1) ^ b) == 1:
                return a + 1
            else:
                return a + 2

        r = len(nums1)
        s = len(nums2)

        # Initialize matrix with zeros: (r+1) x (s+1)
        mat = [[0] * (s + 1) for _ in range(r + 1)]

        # Fill first column
        for u in range(1, r + 1):
            valX = nums1[u - 1]
            mat[u][0] = nxt(mat[u - 1][0], valX)

        # Fill first row
        for v in range(1, s + 1):
            valY = nums2[v - 1]
            mat[0][v] = nxt(mat[0][v - 1], valY)

        # Fill the rest of the matrix
        for iIdx in range(1, r + 1):
            valX_inner = nums1[iIdx - 1]
            for jIdx in range(1, s + 1):
                valY_inner = nums2[jIdx - 1]
                fromLeft = nxt(mat[iIdx - 1][jIdx], valX_inner)
                fromUp = nxt(mat[iIdx][jIdx - 1], valY_inner)
                mat[iIdx][jIdx] = fromLeft if fromLeft < fromUp else fromUp

        return mat[r][s]