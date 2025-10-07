class Solution:
    def maximumHappinessSum(self, happiness, k):
        decrementCounter = 0
        collectedSum = 0
        while decrementCounter < k:
            if decrementCounter == 0:
                self.reorderDescending(happiness)
            tempIndex = decrementCounter
            adjustedValue = happiness[tempIndex] - decrementCounter
            if adjustedValue < 0:
                adjustedValue = 0
            collectedSum += adjustedValue
            decrementCounter += 1
        return collectedSum

    def reorderDescending(self, arr):
        if len(arr) <= 1:
            return
        for left in range(len(arr) - 1):
            for right in range(left + 1, len(arr)):
                if arr[left] < arr[right]:
                    arr[left], arr[right] = arr[right], arr[left]