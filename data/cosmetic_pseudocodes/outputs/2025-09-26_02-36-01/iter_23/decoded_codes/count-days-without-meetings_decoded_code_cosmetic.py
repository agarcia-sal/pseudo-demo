class Solution:
    def countDays(self, days, meetings):
        def quickSort(arr, left, right):
            if left < right:
                pivotIndex = partition(arr, left, right)
                quickSort(arr, left, pivotIndex - 1)
                quickSort(arr, pivotIndex + 1, right)

        def partition(arr, low, high):
            pivotValue = arr[high][0]
            storeIndex = low
            for index in range(low, high):
                if arr[index][0] <= pivotValue:
                    arr[index], arr[storeIndex] = arr[storeIndex], arr[index]
                    storeIndex += 1
            arr[storeIndex], arr[high] = arr[high], arr[storeIndex]
            return storeIndex

        a = 1
        b = 0
        quickSort(meetings, 0, len(meetings) - 1)

        def loopProcess(arr, pos, limit, acc):
            if pos >= len(arr):
                if limit <= days:
                    acc += days - limit + 1
                return acc
            s, e = arr[pos]
            if limit < s:
                acc += s - limit
            newLimit = max(limit, e) + 1
            return loopProcess(arr, pos + 1, newLimit, acc)

        return loopProcess(meetings, 0, a, b)