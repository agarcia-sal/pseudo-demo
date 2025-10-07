class Solution:
    def minLargest(self, nums1: list[int], nums2: list[int]) -> int:
        def nxt(xi: int, yi: int) -> int:
            conditionFlag = ((xi & 1) ^ yi)
            if conditionFlag == 1:
                return xi + 1
            else:
                return xi + 2

        lengthA = len(nums1)
        lengthB = len(nums2)

        # Pad nums1 and nums2 with a leading zero to make indexing 1-based as in pseudocode
        nums1 = [0] + nums1
        nums2 = [0] + nums2

        table = [[0] * (lengthB + 1) for _ in range(lengthA + 1)]

        for rowCounter in range(1, lengthA + 1):
            valX = nums1[rowCounter]
            prevVal = table[rowCounter - 1][0]
            table[rowCounter][0] = nxt(prevVal, valX)

        for colCounter in range(1, lengthB + 1):
            valY = nums2[colCounter]
            prevVal = table[0][colCounter - 1]
            table[0][colCounter] = nxt(prevVal, valY)

        for outerIdx in range(1, lengthA + 1):
            currentX = nums1[outerIdx]
            for innerIdx in range(1, lengthB + 1):
                currentY = nums2[innerIdx]
                candidate1 = nxt(table[outerIdx - 1][innerIdx], currentX)
                candidate2 = nxt(table[outerIdx][innerIdx - 1], currentY)
                table[outerIdx][innerIdx] = candidate1 if candidate1 < candidate2 else candidate2

        return table[lengthA][lengthB]