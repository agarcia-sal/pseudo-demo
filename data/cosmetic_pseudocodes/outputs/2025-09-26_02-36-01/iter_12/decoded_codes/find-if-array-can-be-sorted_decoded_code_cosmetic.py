class Solution:
    def canSortArray(self, nums):
        def bitCount(value):
            counter = 0
            tmp = value
            while tmp != 0:
                counter += tmp & 1
                tmp >>= 1
            return counter

        def swapElements(arrRef, pos1, pos2):
            arrRef[pos1], arrRef[pos2] = arrRef[pos2], arrRef[pos1]

        def partition(arr, startIndex, endIndex):
            pivotVal = arr[endIndex]
            i = startIndex - 1
            j = startIndex
            while j < endIndex:
                if arr[j] <= pivotVal:
                    i += 1
                    swapElements(arr, i, j)
                j += 1
            swapElements(arr, i + 1, endIndex)
            return i + 1

        def quickSortAscending(arr, low, high):
            if low >= high:
                return
            pivotIndex = partition(arr, low, high)
            quickSortAscending(arr, low, pivotIndex - 1)
            quickSortAscending(arr, pivotIndex + 1, high)

        length = len(nums)
        ascending_sorted = []
        for idx in range(length):
            ascending_sorted.append(nums[idx])
        quickSortAscending(ascending_sorted, 0, length - 1)

        outerIndex = 0
        while outerIndex < length:
            innerIndex = 0
            while innerIndex < length - 1:
                if (bitCount(nums[innerIndex]) == bitCount(nums[innerIndex + 1])) and (nums[innerIndex] > nums[innerIndex + 1]):
                    swapElements(nums, innerIndex, innerIndex + 1)
                innerIndex += 1
            outerIndex += 1

        isEqual = True
        compareIdx = 0
        while isEqual and compareIdx < length:
            if nums[compareIdx] != ascending_sorted[compareIdx]:
                isEqual = False
            compareIdx += 1

        return isEqual