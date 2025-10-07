class Solution:
    def minEnd(self, n: int, x: int) -> int:
        def canConstruct(max_val: int) -> bool:
            def checkRec(curVal: int, cntVal: int) -> bool:
                if curVal < max_val:
                    nextVal = curVal + 1
                    if (nextVal & x) == x:
                        newCount = cntVal + 1
                        if newCount == n:
                            return True
                        else:
                            return checkRec(nextVal, newCount)
                    else:
                        return checkRec(nextVal, cntVal)
                else:
                    return cntVal == n
            return checkRec(x, 1)

        def binarySearch(startVal: int, endVal: int) -> int:
            def searchRec(leftCursor: int, rightCursor: int) -> int:
                if leftCursor < rightCursor:
                    midVal = (leftCursor + rightCursor) // 2
                    if canConstruct(midVal):
                        return searchRec(leftCursor, midVal)
                    else:
                        return searchRec(leftCursor + 1, rightCursor)
                else:
                    return leftCursor
            return searchRec(startVal, endVal)

        lowerBound = x
        upperBound = 2 * 10**8
        return binarySearch(lowerBound, upperBound)