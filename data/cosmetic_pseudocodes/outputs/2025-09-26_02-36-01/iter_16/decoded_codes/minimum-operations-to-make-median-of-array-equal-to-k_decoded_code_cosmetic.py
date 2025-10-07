class Solution:
    def minOperationsToMakeMedianK(self, aList, k):
        aList.sort()
        totalCount = len(aList)
        pivotPos = totalCount // 2

        if aList[pivotPos] == k:
            return 0

        tallyOp = 0
        if aList[pivotPos] < k:
            while pivotPos < totalCount and aList[pivotPos] < k:
                tallyOp += k - aList[pivotPos]
                pivotPos += 1
        else:
            while pivotPos >= 0 and aList[pivotPos] > k:
                tallyOp += aList[pivotPos] - k
                pivotPos -= 1

        return tallyOp