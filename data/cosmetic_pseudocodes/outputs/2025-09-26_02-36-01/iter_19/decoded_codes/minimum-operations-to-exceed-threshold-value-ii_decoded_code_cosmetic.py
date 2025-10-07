class Solution:
    def minOperations(self, nums, k):
        def ExtractMin(collection):
            if len(collection) == 0:
                return None
            leastIndex = 0
            currentIndex = 1
            while currentIndex < len(collection):
                if collection[currentIndex] < collection[leastIndex]:
                    leastIndex = currentIndex
                currentIndex += 1
            poppedValue = collection[leastIndex]
            collection[leastIndex] = collection[-1]
            collection.pop()
            RebalanceHeap(collection, leastIndex)
            return poppedValue

        def InsertHeap(collection, value):
            collection.append(value)
            idx = len(collection) - 1
            while idx > 0:
                parentIdx = (idx - 1) // 2
                if collection[parentIdx] > collection[idx]:
                    collection[parentIdx], collection[idx] = collection[idx], collection[parentIdx]
                    idx = parentIdx
                else:
                    break

        def RebalanceHeap(collection, index):
            length = len(collection)
            current = index
            while True:
                leftChild = current * 2 + 1
                rightChild = leftChild + 1
                smallest = current
                if leftChild < length and collection[leftChild] < collection[smallest]:
                    smallest = leftChild
                if rightChild < length and collection[rightChild] < collection[smallest]:
                    smallest = rightChild
                if smallest == current:
                    break
                collection[current], collection[smallest] = collection[smallest], collection[current]
                current = smallest

        def BuildMinHeap(collection):
            startIdx = (len(collection) // 2) - 1
            while startIdx >= 0:
                RebalanceHeap(collection, startIdx)
                startIdx -= 1

        tally = 0
        BuildMinHeap(nums)

        def ConditionCheck():
            return len(nums) > 1 and nums[0] < k

        while ConditionCheck():
            firstPop = ExtractMin(nums)
            secondPop = ExtractMin(nums)
            computedValue = (min(firstPop, secondPop) * 2) + max(firstPop, secondPop)
            InsertHeap(nums, computedValue)
            tally += 1

        return tally