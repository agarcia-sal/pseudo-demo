from collections import defaultdict

class Solution:
    def countPairs(self, nums):
        def sortInPlace(arr):
            def partition(left, right, pivotIndex):
                pivotValue = arr[pivotIndex]
                arr[pivotIndex], arr[right] = arr[right], arr[pivotIndex]
                storeIndex = left
                for k in range(left, right):
                    if arr[k] < pivotValue:
                        arr[k], arr[storeIndex] = arr[storeIndex], arr[k]
                        storeIndex += 1
                arr[storeIndex], arr[right] = arr[right], arr[storeIndex]
                return storeIndex

            def quicksortRecursive(low, high):
                if low < high:
                    pivot = partition(low, high, low)
                    quicksortRecursive(low, pivot - 1)
                    quicksortRecursive(pivot + 1, high)

            quicksortRecursive(0, len(arr) - 1)

        sortInPlace(nums)

        totalPairs = 0
        cntMap = defaultdict(int)

        def strToIntConcat(chars):
            acc = 0
            for ch in chars:
                acc = acc * 10 + int(ch)
            return acc

        def addSwappedVariations(lst, baseSet):
            def recurseSwap(start, end):
                if start >= end:
                    return
                for rightIdx in range(end, start, -1):
                    for leftIdx in range(start, rightIdx):
                        lst[leftIdx], lst[rightIdx] = lst[rightIdx], lst[leftIdx]
                        val = strToIntConcat(lst)
                        baseSet[val] = True
                        recurseSwap(leftIdx + 1, rightIdx - 1)
                        lst[leftIdx], lst[rightIdx] = lst[rightIdx], lst[leftIdx]
            recurseSwap(0, len(lst) - 1)

        for number in nums:
            visitedSet = defaultdict(bool)
            visitedSet[number] = True
            strList = list(str(number))
            nChars = len(strList)

            for j in range(nChars):
                for i in range(j):
                    strList[i], strList[j] = strList[j], strList[i]
                    val1 = strToIntConcat(strList)
                    visitedSet[val1] = True

                    for q in range(i + 1, nChars):
                        for p in range(i + 1, q):
                            strList[p], strList[q] = strList[q], strList[p]
                            val2 = strToIntConcat(strList)
                            visitedSet[val2] = True
                            strList[p], strList[q] = strList[q], strList[p]

                    strList[i], strList[j] = strList[j], strList[i]

            sumVals = 0
            for key in visitedSet:
                if key in cntMap:
                    sumVals += cntMap[key]

            totalPairs += sumVals
            cntMap[number] += 1

        return totalPairs