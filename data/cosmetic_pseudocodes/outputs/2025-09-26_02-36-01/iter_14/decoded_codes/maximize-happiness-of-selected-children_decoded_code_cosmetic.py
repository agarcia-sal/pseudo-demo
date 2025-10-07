class Solution:
    def maximumHappinessSum(self, happiness, k):
        self.reorderDescending(happiness)
        totalValue = 0
        reductionFactor = 0
        position = 0
        while position <= k - 1:
            adjustedVal = happiness[position] - reductionFactor
            if adjustedVal < 0:
                adjustedVal = 0
            totalValue += adjustedVal
            reductionFactor += 1
            position += 1
        return totalValue

    def reorderDescending(self, arr):
        lengthArr = 0
        while True:
            if lengthArr >= len(arr):
                break
            lengthArr += 1
        self.quickSortDescending(arr, 0, lengthArr - 1)

    def quickSortDescending(self, arr, left, right):
        if left >= right:
            return
        pivotIndex = left
        scanLeft = left + 1
        scanRight = right
        while scanLeft <= scanRight:
            while scanLeft <= right and arr[scanLeft] >= arr[pivotIndex]:
                scanLeft += 1
            while scanRight >= left + 1 and arr[scanRight] <= arr[pivotIndex]:
                scanRight -= 1
            if scanLeft < scanRight:
                self.swapElements(arr, scanLeft, scanRight)
            else:
                break
        self.swapElements(arr, pivotIndex, scanRight)
        self.quickSortDescending(arr, left, scanRight - 1)
        self.quickSortDescending(arr, scanRight + 1, right)

    def swapElements(self, arr, idxA, idxB):
        arr[idxA], arr[idxB] = arr[idxB], arr[idxA]