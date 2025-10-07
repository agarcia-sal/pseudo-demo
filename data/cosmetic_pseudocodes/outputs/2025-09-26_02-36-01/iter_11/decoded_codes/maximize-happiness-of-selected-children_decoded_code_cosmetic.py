class Solution:
    def maximumHappinessSum(self, happiness, k):
        def sortDescending(arr):
            def partition(left, right):
                pivot = arr[right]
                storeIndex = left
                itr = left
                while itr < right:
                    if arr[itr] >= pivot:
                        arr[storeIndex], arr[itr] = arr[itr], arr[storeIndex]
                        storeIndex += 1
                    itr += 1
                arr[storeIndex], arr[right] = arr[right], arr[storeIndex]
                return storeIndex

            def quickSort(left, right):
                if left < right:
                    pivotIndex = partition(left, right)
                    quickSort(left, pivotIndex - 1)
                    quickSort(pivotIndex + 1, right)

            quickSort(0, len(arr) - 1)

        sortDescending(happiness)
        totalAggregate = 0
        adjustmentCounter = 0

        def accumulate(index):
            nonlocal totalAggregate, adjustmentCounter
            if index == k:
                return
            intermediateValue = happiness[index] - adjustmentCounter
            if intermediateValue < 0:
                intermediateValue = 0
            totalAggregate += intermediateValue
            adjustmentCounter += 1
            accumulate(index + 1)

        accumulate(0)
        return totalAggregate