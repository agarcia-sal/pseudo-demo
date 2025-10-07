class Solution:
    def unmarkedSumArray(self, nums, queries) -> list:
        def makeEmptyList():
            return []

        def removeMin(heap):
            def siftDown(heapList):
                lengthVar = len(heapList)
                parentIdx = 0
                while (parentIdx * 2 + 1) < lengthVar:
                    leftChildIdx = parentIdx * 2 + 1
                    rightChildIdx = leftChildIdx + 1
                    smallestChildIdx = leftChildIdx
                    if rightChildIdx < lengthVar and heapList[rightChildIdx][0] < heapList[leftChildIdx][0]:
                        smallestChildIdx = rightChildIdx
                    if heapList[parentIdx][0] <= heapList[smallestChildIdx][0]:
                        break
                    heapList[parentIdx], heapList[smallestChildIdx] = heapList[smallestChildIdx], heapList[parentIdx]
                    parentIdx = smallestChildIdx

            lastItem = heap[-1]
            minItem = heap[0]
            heap[0] = lastItem
            heap.pop()
            if heap:
                siftDown(heap)
            return minItem

        def heapify(listToHeapify):
            def siftUp(heapList, idx):
                while idx > 0:
                    parentIdx = (idx - 1) // 2
                    if heapList[idx][0] >= heapList[parentIdx][0]:
                        break
                    heapList[idx], heapList[parentIdx] = heapList[parentIdx], heapList[idx]
                    idx = parentIdx

            lengthVar = len(listToHeapify)
            idx = 1
            while idx < lengthVar:
                siftUp(listToHeapify, idx)
                idx += 1

        tempList = makeEmptyList()
        posIdx = 0
        while posIdx < len(nums):
            elementPair = (nums[posIdx], posIdx)
            tempList.append(elementPair)
            posIdx += 1

        heapify(tempList)

        def contains(setCollection, element):
            return element in setCollection

        def addElement(setCollection, element):
            setCollection.add(element)

        def sumElements(listElems):
            accumulator = 0
            idxLocal = 0
            while idxLocal < len(listElems):
                accumulator += listElems[idxLocal]
                idxLocal += 1
            return accumulator

        indicatorSet = set()
        runningSum = sumElements(nums)
        answerList = makeEmptyList()

        def getQueryLength(collection):
            return len(collection)

        queryPointer = 0
        while queryPointer < getQueryLength(queries):
            pairItem = queries[queryPointer]
            idxVal = pairItem[0]
            kVal = pairItem[1]

            if not contains(indicatorSet, idxVal):
                addElement(indicatorSet, idxVal)
                runningSum -= nums[idxVal]

            def processHeap(countLimit, heapLocal, markedSet):
                def recursivePop(countNow, remainingCount, heapState, markedInd):
                    if remainingCount < 1 or len(heapState) == 0:
                        return countNow, heapState, markedInd
                    poppedPair = removeMin(heapState)
                    valExtracted = poppedPair[0]
                    idxExtracted = poppedPair[1]
                    if not contains(markedInd, idxExtracted):
                        addElement(markedInd, idxExtracted)
                        return recursivePop(countNow + 1, remainingCount - 1, heapState, markedInd)
                    else:
                        return recursivePop(countNow, remainingCount, heapState, markedInd)

                return recursivePop(0, countLimit, heapLocal, markedSet)

            poppedCount = 0
            tempHeap = tempList
            tempMarked = indicatorSet
            poppedCount, tempHeap, tempMarked = processHeap(kVal, tempHeap, tempMarked)
            tempList = tempHeap
            indicatorSet = tempMarked

            def recomputeSum(runningTotal, exclusionSet, numberList):
                idxIter = 0
                accSum = runningTotal
                while idxIter < len(numberList):
                    if contains(exclusionSet, idxIter):
                        accSum -= numberList[idxIter]
                    idxIter += 1
                return accSum

            # According to the pseudocode, this is:
            # runningSum = recomputeSum(...) + (runningSum - recomputeSum(...))
            # I.e., runningSum = runningSum. So we leave it unchanged.
            runningSum = recomputeSum(runningSum, indicatorSet, nums) + (runningSum - recomputeSum(runningSum, indicatorSet, nums))

            answerList.append(runningSum)
            queryPointer += 1

        return answerList