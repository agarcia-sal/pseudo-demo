class Solution:
    def minLargest(self, nums1: list[int], nums2: list[int]) -> int:
        def nxt(x: int, y: int) -> int:
            bitCheck = x & (1 ^ y)
            if bitCheck != 0:
                return x + 1
            else:
                return x + 2

        lengthA = len(nums1)
        lengthB = len(nums2)
        f_matrix = [[0] * (lengthB + 1) for _ in range(lengthA + 1)]

        for counterA in range(1, lengthA + 1):
            valA = nums1[counterA - 1]
            precursor = f_matrix[counterA - 1][0]
            f_matrix[counterA][0] = nxt(precursor, valA)

        for counterB in range(1, lengthB + 1):
            valB = nums2[counterB - 1]
            precursorB = f_matrix[0][counterB - 1]
            f_matrix[0][counterB] = nxt(precursorB, valB)

        for outerIdx in range(1, lengthA + 1):
            currentX = nums1[outerIdx - 1]
            for innerIdx in range(1, lengthB + 1):
                currentY = nums2[innerIdx - 1]

                leftVal = nxt(f_matrix[outerIdx - 1][innerIdx], currentX)
                topVal = nxt(f_matrix[outerIdx][innerIdx - 1], currentY)

                if leftVal <= topVal:
                    f_matrix[outerIdx][innerIdx] = leftVal
                else:
                    f_matrix[outerIdx][innerIdx] = topVal

        return f_matrix[lengthA][lengthB]