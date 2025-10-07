class Solution:
    def minLargest(self, nums1: list[int], nums2: list[int]) -> int:
        def nxt(x: int, y: int) -> int:
            bitCheck = x & (1 ^ y)
            if bitCheck != 0:
                return x + 1
            else:
                return x + 2

        lenA = len(nums1)
        lenB = len(nums2)

        rowCount = lenA + 1
        colCount = lenB + 1
        dp = [[0] * colCount for _ in range(rowCount)]

        def fillRow(posA: int):
            if posA > lenA:
                return
            valA = nums1[posA - 1]
            currentVal = nxt(dp[posA - 1][0], valA)
            dp[posA][0] = currentVal
            fillRow(posA + 1)

        fillRow(1)

        def fillCol(posB: int):
            if posB > lenB:
                return
            valB = nums2[posB - 1]
            currentVal = nxt(dp[0][posB - 1], valB)
            dp[0][posB] = currentVal
            fillCol(posB + 1)

        fillCol(1)

        for iIdx in range(1, lenA + 1):
            valNumA = nums1[iIdx - 1]
            for jIdx in range(1, lenB + 1):
                valNumB = nums2[jIdx - 1]
                option1 = nxt(dp[iIdx - 1][jIdx], valNumA)
                option2 = nxt(dp[iIdx][jIdx - 1], valNumB)
                if option1 < option2:
                    dp[iIdx][jIdx] = option1
                else:
                    dp[iIdx][jIdx] = option2

        return dp[lenA][lenB]