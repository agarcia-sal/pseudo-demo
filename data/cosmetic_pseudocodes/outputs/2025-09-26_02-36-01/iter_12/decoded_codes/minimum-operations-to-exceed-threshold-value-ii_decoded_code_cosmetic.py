class Solution:
    def minOperations(self, nums, k):
        # Helper functions to implement a min-heap using a list

        def popMin(collection):
            size = len(collection)
            if size == 0:
                return None
            last = collection[-1]
            collection[0], collection[-1] = collection[-1], collection[0]
            collection.pop()

            parent = 0
            child = 1
            while child < len(collection):
                if child + 1 < len(collection) and collection[child + 1] < collection[child]:
                    child += 1
                if collection[parent] <= collection[child]:
                    break
                collection[parent], collection[child] = collection[child], collection[parent]
                parent = child
                child = 2 * parent + 1
            return last

        def insertValue(collection, val):
            collection.append(val)
            idx = len(collection) - 1
            while idx > 0:
                parentIdx = (idx - 1) // 2
                if collection[parentIdx] <= collection[idx]:
                    break
                collection[parentIdx], collection[idx] = collection[idx], collection[parentIdx]
                idx = parentIdx

        def buildHeap(collection):
            start = (len(collection) // 2) - 1
            while start >= 0:
                root = start
                while True:
                    child = 2 * root + 1
                    if child >= len(collection):
                        break
                    if child + 1 < len(collection) and collection[child + 1] < collection[child]:
                        child += 1
                    if collection[root] <= collection[child]:
                        break
                    collection[root], collection[child] = collection[child], collection[root]
                    root = child
                start -= 1

        buildHeap(nums)

        counter = 0
        conditionFulfilled = True

        while conditionFulfilled:
            cond1 = len(nums) > 1
            cond2 = len(nums) > 0 and nums[0] < k
            conditionFulfilled = cond1 and cond2
            if not conditionFulfilled:
                break

            firstMin = popMin(nums)
            secondMin = popMin(nums)
            smaller, bigger = (firstMin, secondMin) if firstMin <= secondMin else (secondMin, firstMin)
            computedValue = (smaller + smaller) + bigger
            insertValue(nums, computedValue)
            counter += 1

        return counter