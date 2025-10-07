class Solution:
    def minLargest(self, nums1: list[int], nums2: list[int]) -> int:
        def nxt(xval: int, yval: int) -> int:
            if (xval & (1 ^ yval)) == 1:
                return xval + 1
            else:
                return xval + 2

        lengthA = len(nums1)
        lengthB = len(nums2)
        matrix = [[0] * (lengthB + 1) for _ in range(lengthA + 1)]

        def fillRow(i: int) -> None:
            if i > lengthA:
                return
            currentA = nums1[i - 1]
            prevVal = matrix[i - 1][0]
            matrix[i][0] = nxt(prevVal, currentA)
            fillRow(i + 1)

        fillRow(1)

        def fillCol(j: int) -> None:
            if j > lengthB:
                return
            currentB = nums2[j - 1]
            prevValB = matrix[0][j - 1]
            matrix[0][j] = nxt(prevValB, currentB)
            fillCol(j + 1)

        fillCol(1)

        def fillMatrix(i: int, j: int) -> None:
            if i > lengthA:
                return
            if j > lengthB:
                fillMatrix(i + 1, 1)
                return

            valA = nums1[i - 1]
            valB = nums2[j - 1]
            topVal = matrix[i - 1][j]
            leftVal = matrix[i][j - 1]
            candidate1 = nxt(topVal, valA)
            candidate2 = nxt(leftVal, valB)
            matrix[i][j] = candidate1 if candidate1 <= candidate2 else candidate2
            fillMatrix(i, j + 1)

        fillMatrix(1, 1)
        return matrix[lengthA][lengthB]