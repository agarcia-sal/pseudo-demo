class Solution:
    def maximumHappinessSum(self, happiness, k):
        def arrangeDescending(arr):
            def exchanger(x, y):
                arr[x], arr[y] = arr[y], arr[x]

            m = len(arr)

            def partition(lo, hi):
                pivotIndex = lo
                pivotVal = arr[hi]
                storeIndex = lo
                while pivotIndex < hi:
                    if arr[pivotIndex] >= pivotVal:
                        exchanger(storeIndex, pivotIndex)
                        storeIndex += 1
                    pivotIndex += 1
                exchanger(storeIndex, hi)
                return storeIndex

            def quickSort(lo, hi):
                if lo < hi:
                    p = partition(lo, hi)
                    quickSort(lo, p - 1)
                    quickSort(p + 1, hi)

            quickSort(0, m - 1)

        arrangeDescending(happiness)

        accumulatorTotal = 0
        decreaseCounter = 0

        def sumLoop(currIndex):
            nonlocal accumulatorTotal, decreaseCounter
            if currIndex >= k:
                return
            adjustedValue = happiness[currIndex] - decreaseCounter
            if adjustedValue < 0:
                adjustedValue = 0
            accumulatorTotal += adjustedValue
            decreaseCounter += 1
            sumLoop(currIndex + 1)

        sumLoop(0)

        return accumulatorTotal