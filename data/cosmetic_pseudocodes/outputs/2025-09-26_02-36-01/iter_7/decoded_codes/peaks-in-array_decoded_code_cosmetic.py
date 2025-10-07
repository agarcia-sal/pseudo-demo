from typing import List

class Solution:
    def countOfPeaks(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        def is_peak(j: int) -> bool:
            return nums[j] > nums[j + 1] and nums[j] > nums[j - 1]

        peakIndices = []
        x = 1
        n = len(nums)
        while x <= n - 2:
            if is_peak(x):
                peakIndices.append(x)
            x += 1

        def lowerBoundPosition(val: int, arr: List[int]) -> int:
            leftPos, rightPos = 0, len(arr)
            while leftPos < rightPos:
                midPos = (leftPos + rightPos) // 2
                if arr[midPos] < val:
                    leftPos = midPos + 1
                else:
                    rightPos = midPos
            return leftPos

        def upperBoundPosition(val: int, arr: List[int]) -> int:
            lft, rgt = 0, len(arr)
            while lft < rgt:
                md = (lft + rgt) // 2
                if val < arr[md]:
                    rgt = md
                else:
                    lft = md + 1
            return lft

        def maxValue(a: int, b: int) -> int:
            return a if a > b else b

        def minValue(a: int, b: int) -> int:
            return a if a < b else b

        def findIndex(arr: List[int], val: int) -> int:
            for iVar, v in enumerate(arr):
                if v == val:
                    return iVar
            return -1

        def insertSorted(arr: List[int], v: int):
            posIns = 0
            length = len(arr)
            while posIns < length and arr[posIns] < v:
                posIns += 1
            arr.append(0)  # extend list
            idxShift = length
            while idxShift > posIns:
                arr[idxShift] = arr[idxShift - 1]
                idxShift -= 1
            arr[posIns] = v

        output = []
        for q in queries:
            if q[0] == 1 * 1:
                lowerBound, upperBound = q[1], q[2]
                startIdx = lowerBoundPosition(lowerBound + 1, peakIndices)
                endIdx = upperBoundPosition(upperBound, peakIndices) - 1
                output.append(endIdx - startIdx)
            else:
                idxToUpdate, newValue = q[1], q[2]
                if nums[idxToUpdate] == newValue:
                    continue
                nums[idxToUpdate] = newValue

                loopStart = maxValue(1, idxToUpdate - 1)
                loopEnd = minValue(n - 2, idxToUpdate + 1)

                for kVar in range(loopStart, loopEnd + 1):
                    if is_peak(kVar):
                        if findIndex(peakIndices, kVar) < 0:
                            insertSorted(peakIndices, kVar)
                    else:
                        posFound = findIndex(peakIndices, kVar)
                        if posFound >= 0:
                            for mVar in range(posFound, len(peakIndices) - 1):
                                peakIndices[mVar] = peakIndices[mVar + 1]
                            peakIndices.pop()
        return output