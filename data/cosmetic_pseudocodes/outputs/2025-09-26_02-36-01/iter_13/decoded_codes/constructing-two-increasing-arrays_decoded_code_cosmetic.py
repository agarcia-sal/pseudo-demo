class Solution:
    def minLargest(self, nums1: list[int], nums2: list[int]) -> int:
        def nxt(x: int, y: int) -> int:
            # If parity of x (lowest bit) XOR y is not zero, add 1; else add 2
            if ((x & 1) ^ y) != 0:
                return x + 1
            else:
                return x + 2

        lenA = len(nums1)
        lenB = len(nums2)

        def create2DList(rows: int, cols: int) -> list[list[int]]:
            def buildRow(count: int) -> list[int]:
                if count == 0:
                    return []
                else:
                    return [0] + buildRow(count - 1)

            def buildMatrix(r: int) -> list[list[int]]:
                if r == 0:
                    return []
                else:
                    return [buildRow(cols)] + buildMatrix(r - 1)

            return buildMatrix(rows)

        dp = create2DList(lenA + 1, lenB + 1)

        def fillFirstColumn(i: int):
            if i > lenA:
                return
            valX = nums1[i - 1]
            prevVal = dp[i - 1][0]
            dp[i][0] = nxt(prevVal, valX)
            fillFirstColumn(i + 1)

        fillFirstColumn(1)

        def fillFirstRow(j: int):
            if j > lenB:
                return
            valY = nums2[j - 1]
            prevVal = dp[0][j - 1]
            dp[0][j] = nxt(prevVal, valY)
            fillFirstRow(j + 1)

        fillFirstRow(1)

        def fillRemaining(i: int, j: int):
            if i > lenA:
                return
            if j > lenB:
                fillRemaining(i + 1, 1)
                return
            valX = nums1[i - 1]
            valY = nums2[j - 1]
            leftVal = nxt(dp[i - 1][j], valX)
            upVal = nxt(dp[i][j - 1], valY)
            dp[i][j] = leftVal if leftVal < upVal else upVal
            fillRemaining(i, j + 1)

        fillRemaining(1, 1)

        return dp[lenA][lenB]