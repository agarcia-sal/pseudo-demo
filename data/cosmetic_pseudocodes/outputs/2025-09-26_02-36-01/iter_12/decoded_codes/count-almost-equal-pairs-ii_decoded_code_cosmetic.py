from collections import defaultdict

class Solution:
    def countPairs(self, nums):
        def replicateSort(array):
            def quickPartition(arr, low, high):
                pivot_val = arr[high]

                def swapElements(arr, idx1, idx2):
                    arr[idx1], arr[idx2] = arr[idx2], arr[idx1]

                pointer = low
                for walker in range(low, high):
                    if arr[walker] <= pivot_val:
                        swapElements(arr, walker, pointer)
                        pointer += 1
                swapElements(arr, pointer, high)
                return pointer

            def quickSortHelper(arr, left, right):
                if left < right:
                    split_point = quickPartition(arr, left, right)
                    quickSortHelper(arr, left, split_point - 1)
                    quickSortHelper(arr, split_point + 1, right)

            quickSortHelper(array, 0, len(array) - 1)

        replicateSort(nums)

        totalPairs = 0
        frequencyMap = defaultdict(int)

        def integerJoin(charList):
            return int(''.join(charList))

        def swapByIndices(collection, idxA, idxB):
            collection[idxA], collection[idxB] = collection[idxB], collection[idxA]

        def addAllFromSetToSum(freqMap, valuesSet):
            return sum(freqMap[item] for item in valuesSet if item in freqMap)

        def generateAllVariations(numStr, currentIndex, visSet):
            if currentIndex >= len(numStr):
                return
            for forwardIdx in range(len(numStr) - 1, currentIndex, -1):
                swapByIndices(numStr, currentIndex, forwardIdx)
                visSet.add(integerJoin(numStr))
                for backwardIdx in range(currentIndex + 1, forwardIdx):
                    swapByIndices(numStr, backwardIdx, forwardIdx)
                    visSet.add(integerJoin(numStr))
                    swapByIndices(numStr, backwardIdx, forwardIdx)
                swapByIndices(numStr, currentIndex, forwardIdx)
            generateAllVariations(numStr, currentIndex + 1, visSet)

        def iterateOverElements(collection):
            next_index = 0
            while next_index < len(collection):
                yield collection[next_index]
                next_index += 1

        for element in iterateOverElements(nums):
            visitedValues = set()
            visitedValues.add(element)
            elementStringList = list(str(element))
            generateAllVariations(elementStringList, 0, visitedValues)
            totalPairs += addAllFromSetToSum(frequencyMap, visitedValues)
            frequencyMap[element] += 1

        return totalPairs