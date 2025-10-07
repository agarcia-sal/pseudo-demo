class Solution:
    def unmarkedSumArray(self, nums, queries):
        helperHeap = []

        def siftDown(heapArray, startIdx, heapSize):
            parent = startIdx
            while True:
                leftChild = 2 * parent + 1
                rightChild = 2 * parent + 2
                smallest = parent

                if leftChild < heapSize and heapArray[leftChild][0] < heapArray[smallest][0]:
                    smallest = leftChild
                if rightChild < heapSize and heapArray[rightChild][0] < heapArray[smallest][0]:
                    smallest = rightChild
                if smallest == parent:
                    return
                heapArray[parent], heapArray[smallest] = heapArray[smallest], heapArray[parent]
                parent = smallest

        def buildHeap(arr):
            n = len(arr)
            p = (n // 2) - 1
            while p >= 0:
                siftDown(arr, p, n)
                p -= 1

        def extractMin(heapArray):
            if not heapArray:
                return None
            root = heapArray[0]
            heapArray[0] = heapArray[-1]
            heapArray.pop()
            if heapArray:
                siftDown(heapArray, 0, len(heapArray))
            return root

        for idxElem, valElem in enumerate(nums):
            helperHeap.append([valElem, idxElem])
        buildHeap(helperHeap)

        flaggedIndices = set()
        cumulativeSum = sum(nums)
        answerList = []

        queryIterator = 0
        while queryIterator < len(queries):
            iterIdx, iterK = queries[queryIterator]

            if iterIdx not in flaggedIndices:
                flaggedIndices.add(iterIdx)
                cumulativeSum -= nums[iterIdx]

            loopCount = 0
            while loopCount < iterK:
                if not helperHeap:
                    break
                candidate = extractMin(helperHeap)
                if candidate is None:
                    break
                candidateVal, candidateIdx = candidate
                if candidateIdx not in flaggedIndices:
                    flaggedIndices.add(candidateIdx)
                    cumulativeSum -= candidateVal
                    loopCount += 1

            answerList.append(cumulativeSum)
            queryIterator += 1

        return answerList