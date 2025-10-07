class Solution:

    def maxTotalReward(self, rewardValues):

        def auxiliaryTraverse(currentSum):

            def findInsertionIndex(array, target):
                lowBoundary = 0
                highBoundary = len(array)
                while lowBoundary < highBoundary:
                    midpoint = lowBoundary + ((highBoundary - lowBoundary) // 2)
                    if target < array[midpoint]:
                        highBoundary = midpoint
                    else:
                        lowBoundary = midpoint + 1
                return lowBoundary

            startIndex = findInsertionIndex(rewardValues, currentSum)
            accumulatedMaximum = 0
            indexCounter = startIndex

            while indexCounter < len(rewardValues):
                candidateValue = rewardValues[indexCounter]
                if not ((currentSum + candidateValue) <= currentSum):
                    recursiveResult = auxiliaryTraverse(currentSum + candidateValue)
                    candidateTotal = candidateValue + recursiveResult
                    if candidateTotal > accumulatedMaximum:
                        accumulatedMaximum = candidateTotal
                indexCounter += 1

            return accumulatedMaximum

        def ascendingSort(arr):
            def swapElements(i, j):
                arr[i], arr[j] = arr[j], arr[i]

            def partition(low, high):
                pivotValue = arr[high]
                pointer = low - 1
                iterIdx = low

                while iterIdx < high:
                    if arr[iterIdx] <= pivotValue:
                        pointer += 1
                        swapElements(pointer, iterIdx)
                    iterIdx += 1

                swapElements(pointer + 1, high)
                return pointer + 1

            def quickSortRec(low, high):
                if low < high:
                    partitionIndex = partition(low, high)
                    quickSortRec(low, partitionIndex - 1)
                    quickSortRec(partitionIndex + 1, high)

            quickSortRec(0, len(arr) - 1)

        ascendingSort(rewardValues)
        return auxiliaryTraverse(0)