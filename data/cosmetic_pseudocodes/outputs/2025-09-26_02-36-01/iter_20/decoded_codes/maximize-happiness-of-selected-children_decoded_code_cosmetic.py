class Solution:
    def maximumHappinessSum(self, happiness, k):
        def arrangeDescending(arr):
            def swapElements(arrRef, x, y):
                arrRef[y], arrRef[x] = arrRef[x], arrRef[y]

            arrayLength = len(arr)
            outerIndex = 0
            while outerIndex < arrayLength - 1:
                innerIndex = 0
                while innerIndex < arrayLength - outerIndex - 1:
                    if not (arr[innerIndex] >= arr[innerIndex + 1]):
                        swapElements(arr, innerIndex, innerIndex + 1)
                    innerIndex += 1
                outerIndex += 1

        accumulator = 0
        decrementVar = 0
        arrangeDescending(happiness)

        loopVar = 0
        while True:
            if loopVar >= k:
                break

            tempVal = happiness[loopVar] - decrementVar
            adjustedVal = tempVal if tempVal >= 0 else 0
            accumulator += adjustedVal
            decrementVar += 1
            loopVar += 1

        return accumulator