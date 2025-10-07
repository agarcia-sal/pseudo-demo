class Solution:
    def minMoves(self, rooks):
        totalElements = len(rooks)
        firstSort = self.CustomSort(rooks, self.getFirst)
        secondSort = self.CustomSort(rooks, self.getSecond)
        aggregateMoves = 0
        pos = 0
        while pos < totalElements:
            currentItem = firstSort[pos]
            tempDiff = abs(currentItem[0] - pos)
            aggregateMoves += tempDiff
            pos += 1
        columnAccumulator = 0
        pointer = 0
        while True:
            if pointer == totalElements:
                break
            elementAtPointer = secondSort[pointer]
            absoluteDelta = self.ComputeAbsDifference(elementAtPointer[1], pointer)
            columnAccumulator += absoluteDelta
            pointer += 1
        return aggregateMoves + columnAccumulator

    def CustomSort(self, collection, keyFunc):
        return self.MergeSort(collection, keyFunc)

    def getFirst(self, pair):
        return pair[0]

    def getSecond(self, pair):
        return pair[1]

    def ComputeAbsDifference(self, a, b):
        if a >= b:
            return a - b
        else:
            return b - a

    def MergeSort(self, arr, key):
        if len(arr) <= 1:
            return arr
        middleIndex = len(arr) // 2
        leftArray = arr[:middleIndex]
        rightArray = arr[middleIndex:]
        sortedLeft = self.MergeSort(leftArray, key)
        sortedRight = self.MergeSort(rightArray, key)
        return self.Merge(sortedLeft, sortedRight, key)

    def Merge(self, leftArr, rightArr, keyFunc):
        resultArr = []
        leftIdx = 0
        rightIdx = 0
        while leftIdx < len(leftArr) and rightIdx < len(rightArr):
            if keyFunc(leftArr[leftIdx]) <= keyFunc(rightArr[rightIdx]):
                resultArr.append(leftArr[leftIdx])
                leftIdx += 1
            else:
                resultArr.append(rightArr[rightIdx])
                rightIdx += 1
        while leftIdx < len(leftArr):
            resultArr.append(leftArr[leftIdx])
            leftIdx += 1
        while rightIdx < len(rightArr):
            resultArr.append(rightArr[rightIdx])
            rightIdx += 1
        return resultArr