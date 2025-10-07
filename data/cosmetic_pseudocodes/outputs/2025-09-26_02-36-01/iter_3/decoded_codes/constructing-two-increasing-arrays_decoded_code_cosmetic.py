class Solution:
    def minLargest(self, nums1: list[int], nums2: list[int]) -> int:
        def nxt(x: int, y: int) -> int:
            bit_check = x & (1 ^ y)
            if bit_check != 0:
                return x + 1
            else:
                return x + 2

        lenA = len(nums1)
        lenB = len(nums2)

        matrix = []
        for _ in range(lenA + 1):
            matrix.append([0] * (lenB + 1))

        for i in range(1, lenA + 1):
            valA = nums1[i - 1]
            prevVal = matrix[i - 1][0]
            matrix[i][0] = nxt(prevVal, valA)

        for j in range(1, lenB + 1):
            valB = nums2[j - 1]
            prevVal = matrix[0][j - 1]
            matrix[0][j] = nxt(prevVal, valB)

        for i in range(1, lenA + 1):
            xVal = nums1[i - 1]
            for j in range(1, lenB + 1):
                yVal = nums2[j - 1]
                fromAbove = nxt(matrix[i - 1][j], xVal)
                fromLeft = nxt(matrix[i][j - 1], yVal)
                matrix[i][j] = fromAbove if fromAbove < fromLeft else fromLeft

        return matrix[lenA][lenB]