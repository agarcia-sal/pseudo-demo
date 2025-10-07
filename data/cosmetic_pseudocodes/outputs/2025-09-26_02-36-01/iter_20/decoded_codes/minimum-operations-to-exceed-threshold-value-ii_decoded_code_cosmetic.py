class Solution:
    def minOperations(self, nums, k):
        def customHeapify(collection):
            for index in range(len(collection) // 2, -1, -1):
                customSiftDown(collection, index)

        def customSiftDown(heap, start):
            heapSize = len(heap)
            idx = start
            while True:
                leftChild = 2 * idx + 1
                rightChild = leftChild + 1
                smallest = idx

                if leftChild < heapSize and heap[leftChild] < heap[smallest]:
                    smallest = leftChild
                if rightChild < heapSize and heap[rightChild] < heap[smallest]:
                    smallest = rightChild

                if smallest == idx:
                    break

                heap[idx], heap[smallest] = heap[smallest], heap[idx]
                idx = smallest

        def customHeappop(heap):
            root = heap[0]
            lastElement = heap[-1]
            heap[0] = lastElement
            heap.pop()
            if heap:
                customSiftDown(heap, 0)
            return root

        def customHeappush(heap, val):
            heap.append(val)
            currentIdx = len(heap) - 1
            while currentIdx > 0:
                parentIdx = (currentIdx - 1) // 2
                if heap[parentIdx] <= heap[currentIdx]:
                    break
                heap[parentIdx], heap[currentIdx] = heap[currentIdx], heap[parentIdx]
                currentIdx = parentIdx

        customHeapify(nums)
        countOps = 0

        while True:
            if not (nums[0] < k and len(nums) > 1):
                break

            firstVal = customHeappop(nums)
            secondVal = customHeappop(nums)
            computedVal = (min(firstVal, secondVal) * 2) + max(firstVal, secondVal)
            customHeappush(nums, computedVal)
            countOps += 1

        return countOps