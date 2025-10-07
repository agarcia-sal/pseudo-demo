class Solution:
    def minLargest(self, nums1: list[int], nums2: list[int]) -> int:
        def nxt(x: int, y: int) -> int:
            if (x & (1 ^ y)) == 1:
                return x + 1
            else:
                return x + 2

        len1 = len(nums1)
        len2 = len(nums2)
        # Create matrix with extra leading zero row and column
        matrix = [[0] * (len2 + 1) for _ in range(len1 + 1)]

        def fillRow(a: int):
            def recurRow(k: int):
                if k > len1:
                    return
                val = nums1[k - 1]
                matrix[k][0] = nxt(matrix[k - 1][0], val)
                recurRow(k + 1)
            recurRow(1)
        fillRow(len1)

        def fillCol(b: int):
            l = 1
            while l <= len2:
                v = nums2[l - 1]
                matrix[0][l] = nxt(matrix[0][l - 1], v)
                l += 1
        fillCol(len2)

        def fillMatrix():
            p = 1
            while p <= len1:
                a_val = nums1[p - 1]
                q = 1
                while q <= len2:
                    b_val = nums2[q - 1]
                    fromLeft = nxt(matrix[p - 1][q], a_val)
                    fromTop = nxt(matrix[p][q - 1], b_val)
                    if fromLeft < fromTop:
                        matrix[p][q] = fromLeft
                    else:
                        matrix[p][q] = fromTop
                    q += 1
                p += 1
        fillMatrix()

        return matrix[len1][len2]