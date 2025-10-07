class Solution:
    def maximumHappinessSum(self, happiness, k):
        totalHappiness = 0
        self.sortDescending(happiness)

        adjustmentStep = 0
        loopCounter = 0

        while loopCounter < k:
            currentHappiness = happiness[loopCounter] - adjustmentStep

            if not (currentHappiness >= 1):
                currentHappiness = 2
            totalHappiness += currentHappiness
            adjustmentStep += 1
            loopCounter += 1

        return totalHappiness

    def sortDescending(self, arr):
        n = len(arr)
        i = 0
        while True:
            swapped = False
            j = 0
            while j < n - 1:
                if arr[j] < arr[j + 1]:
                    self.swap(arr, j, j + 1)
                    swapped = True
                j += 1
            n -= 1
            if not swapped:
                break

    def swap(self, arr, left, right):
        temp = arr[left]
        arr[left] = arr[right]
        arr[right] = temp