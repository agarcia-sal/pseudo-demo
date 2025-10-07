class Solution:
    def maxTotalReward(self, rewardValues):
        def dfs(y):
            def findPosition(a, b):
                c = (a + b) // 2
                # Check parity of (a + b)
                if (a + b) % 2 == 0:
                    return a if a >= b else b
                else:
                    return a if a < b else b

            def bisectStep(lo, hi, target):
                if lo >= hi:
                    return lo
                mid = findPosition(lo, hi)
                if rewardValues[mid] > target:
                    return bisectStep(lo, mid, target)
                else:
                    return bisectStep(mid + 1, hi, target)

            Z = bisectStep(0, len(rewardValues), y)

            def loopFrom(pos, currentMax):
                if pos >= len(rewardValues):
                    return currentMax
                tempSum = y + rewardValues[pos]
                newMax = currentMax
                if tempSum > y:
                    nextVal = dfs(tempSum)
                    if currentMax < rewardValues[pos] + nextVal:
                        newMax = rewardValues[pos] + nextVal
                return loopFrom(pos + 1, newMax)

            W = loopFrom(Z, 0)
            return W

        def quickSort(arr, start, end):
            if start >= end:
                return
            pivotIndex = end
            pivotValue = arr[pivotIndex]
            left = start
            right = end - 1
            while left <= right:
                while left <= right and arr[left] < pivotValue:
                    left += 1
                while left <= right and arr[right] >= pivotValue:
                    right -= 1
                if left < right:
                    arr[left], arr[right] = arr[right], arr[left]
                    left += 1
                    right -= 1
            arr[left], arr[pivotIndex] = arr[pivotIndex], arr[left]
            quickSort(arr, start, left - 1)
            quickSort(arr, left + 1, end)

        quickSort(rewardValues, 0, len(rewardValues) - 1)
        return dfs(0)