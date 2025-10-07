from collections import defaultdict

class Solution:
    def countPairs(self, nums):
        def customSort(arr):
            def partition(lo, hi):
                pivotValue = arr[hi]
                splitIndex = lo - 1
                for scanIndex in range(lo, hi):
                    if arr[scanIndex] <= pivotValue:
                        splitIndex += 1
                        swap(splitIndex, scanIndex)
                swap(splitIndex + 1, hi)
                return splitIndex + 1

            def swap(i1, i2):
                arr[i1], arr[i2] = arr[i2], arr[i1]

            def quickSortHelper(leftBound, rightBound):
                if leftBound < rightBound:
                    pi = partition(leftBound, rightBound)
                    quickSortHelper(leftBound, pi - 1)
                    quickSortHelper(pi + 1, rightBound)

            quickSortHelper(0, len(arr) - 1)

        customSort(nums)

        resultCount = 0
        frequencyMap = defaultdict(int)

        def addPermutations(num):
            seenSet = set()
            seenSet.add(num)
            strList = []

            def intToStringList(n, lst):
                if n == 0:
                    return
                intToStringList(n // 10, lst)
                lst.append(chr((n % 10) + 48))

            intToStringList(num, strList)
            if not strList:
                strList.append('0')
            lenStrList = len(strList)

            def addNumberFromList(lst):
                totalNum = 0
                for ch in lst:
                    totalNum = totalNum * 10 + (ord(ch) - 48)
                return totalNum

            def swapPositions(a, b):
                strList[a], strList[b] = strList[b], strList[a]

            def recurseSwap(startPos, endPos):
                if startPos >= endPos:
                    return
                for currentJ in range(endPos, startPos, -1):
                    for currentI in range(startPos, currentJ):
                        swapPositions(currentI, currentJ)
                        seenSet.add(addNumberFromList(strList))
                        for qIndex in range(currentI + 1, lenStrList):
                            for pIndex in range(currentI + 1, qIndex):
                                swapPositions(pIndex, qIndex)
                                seenSet.add(addNumberFromList(strList))
                                swapPositions(pIndex, qIndex)
                        swapPositions(currentI, currentJ)

            recurseSwap(0, lenStrList - 1)
            return seenSet

        for element in nums:
            permutationsSet = addPermutations(element)
            sumForCurrent = 0
            for key in permutationsSet:
                if key in frequencyMap:
                    sumForCurrent += frequencyMap[key]
            resultCount += sumForCurrent
            frequencyMap[element] += 1

        return resultCount