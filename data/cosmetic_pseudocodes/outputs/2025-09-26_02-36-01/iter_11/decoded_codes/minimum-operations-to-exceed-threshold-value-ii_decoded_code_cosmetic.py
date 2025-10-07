class Solution:
    def minOperations(self, k, nums):
        def extractMin(collection):
            value = collection[0]
            lastIndex = len(collection) - 1
            collection[0] = collection[lastIndex]
            collection.pop()
            current = 0
            size = len(collection)
            while True:
                leftChild = 2 * current + 1
                rightChild = 2 * current + 2
                if leftChild >= size:
                    break
                smallestChild = leftChild
                if rightChild < size and collection[rightChild] < collection[leftChild]:
                    smallestChild = rightChild
                if collection[current] <= collection[smallestChild]:
                    break
                collection[current], collection[smallestChild] = collection[smallestChild], collection[current]
                current = smallestChild
            return value

        def insertHeap(collection, value):
            collection.append(value)
            idx = len(collection) - 1
            while idx > 0:
                parentIdx = (idx - 1) // 2
                if collection[parentIdx] <= collection[idx]:
                    break
                collection[parentIdx], collection[idx] = collection[idx], collection[parentIdx]
                idx = parentIdx

        def siftDown(collection, startIndex, heapSize):
            root = startIndex
            while True:
                child_left = 2 * root + 1
                if child_left >= heapSize:
                    break
                swapIdx = root
                if collection[swapIdx] > collection[child_left]:
                    swapIdx = child_left
                child_right = child_left + 1
                if child_right < heapSize and collection[swapIdx] > collection[child_right]:
                    swapIdx = child_right
                if swapIdx == root:
                    break
                collection[root], collection[swapIdx] = collection[swapIdx], collection[root]
                root = swapIdx

        def buildHeap(collection):
            start = (len(collection) // 2) - 1
            while start >= 0:
                siftDown(collection, start, len(collection))
                start -= 1

        buildHeap(nums)
        counter = 0
        while True:
            if len(nums) <= 1:
                break
            if not (nums[0] < k):
                break

            firstElem = extractMin(nums)
            secondElem = extractMin(nums)

            partialMin = firstElem if firstElem <= secondElem else secondElem
            partialMax = firstElem if firstElem >= secondElem else secondElem

            mergedVal = (partialMin * 2) + partialMax
            insertHeap(nums, mergedVal)
            counter += 1

        return counter