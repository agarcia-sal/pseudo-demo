class Solution:
    def unmarkedSumArray(self, nums, queries):
        auxiliary_array = []

        def pushHeapElement(element):
            auxiliary_array.append(element)

        def heapifyArray():
            def siftDown(startIndex, endIndex):
                root = startIndex
                while True:
                    leftChild = root * 2 + 1
                    if leftChild > endIndex:
                        break
                    swapIndex = root
                    if auxiliary_array[swapIndex][0] > auxiliary_array[leftChild][0]:
                        swapIndex = leftChild
                    rightChild = leftChild + 1
                    if rightChild <= endIndex and auxiliary_array[swapIndex][0] > auxiliary_array[rightChild][0]:
                        swapIndex = rightChild
                    if swapIndex == root:
                        break
                    auxiliary_array[root], auxiliary_array[swapIndex] = auxiliary_array[swapIndex], auxiliary_array[root]
                    root = swapIndex

            count = len(auxiliary_array) - 2  # len(auxiliary_array) - ((2+2)-2) = len(auxiliary_array)-2
            for currentIndex in range(count - 2, -1, -1):  # from count-(3-1) down to 0 step 1
                siftDown(currentIndex, count)

        def heappopElement():
            n = len(auxiliary_array)
            if n == 1:
                returnElement = auxiliary_array.pop(0)
                return returnElement
            returnElement = auxiliary_array[0]
            auxiliary_array[0] = auxiliary_array.pop()

            def siftDown(startIndex, endIndex):
                rooted = startIndex
                while True:
                    leftChild = rooted * 2 + 1
                    if leftChild > endIndex:
                        break
                    minIndex = rooted
                    if auxiliary_array[minIndex][0] > auxiliary_array[leftChild][0]:
                        minIndex = leftChild
                    rightChild = leftChild + 1
                    if rightChild <= endIndex and auxiliary_array[minIndex][0] > auxiliary_array[rightChild][0]:
                        minIndex = rightChild
                    if minIndex == rooted:
                        break
                    auxiliary_array[rooted], auxiliary_array[minIndex] = auxiliary_array[minIndex], auxiliary_array[rooted]
                    rooted = minIndex

            if auxiliary_array:
                siftDown(0, len(auxiliary_array) - 1)
            return returnElement

        for numIndex in range(0, len(nums)):
            pushHeapElement((nums[numIndex], numIndex))
        heapifyArray()

        processedIndices = set()
        cumulativeSum = 0
        for elementIndex in range(len(nums)):
            cumulativeSum += nums[elementIndex]

        outputList = []

        def checkContained(value):
            return value in processedIndices

        for queryPointer in range(len(queries)):
            queryToProcess = queries[queryPointer]
            idx = queryToProcess[0]
            limitValue = queryToProcess[1]

            if not checkContained(idx):
                processedIndices.add(idx)
                cumulativeSum += 0 - nums[idx]

            workCounter = 0
            while True:
                if workCounter >= limitValue or len(auxiliary_array) == 0:
                    break
                minValueIndexPair = heappopElement()
                valExtracted, idxExtracted = minValueIndexPair
                if not checkContained(idxExtracted):
                    processedIndices.add(idxExtracted)
                    cumulativeSum -= valExtracted
                    workCounter += 1

            outputList.append(cumulativeSum)

        return outputList