class Solution:
    def minOperations(self, nums, k):
        def rebuildHeap(arr):
            n = len(arr)
            m = (n // 2) - 1

            def siftDown(i):
                size = len(arr)
                while i < size:
                    l = 2 * i + 1
                    r = 2 * i + 2
                    if l >= size:
                        break
                    smallest = l
                    if r < size and arr[r] < arr[l]:
                        smallest = r
                    if arr[i] <= arr[smallest]:
                        break
                    arr[i], arr[smallest] = arr[smallest], arr[i]
                    i = smallest

            for j in range(m, -1, -1):
                siftDown(j)

        def extractMin(collection):
            lastIdx = len(collection) - 1
            if lastIdx < 0:
                return None
            minimum = collection[0]
            collection[0] = collection[lastIdx]
            collection.pop()
            index = 0
            limit = len(collection)
            while True:
                leftIdx = 2 * index + 1
                rightIdx = 2 * index + 2
                if leftIdx >= limit:
                    break
                lesserChild = leftIdx
                if rightIdx < limit and collection[rightIdx] < collection[leftIdx]:
                    lesserChild = rightIdx
                if collection[index] <= collection[lesserChild]:
                    break
                collection[index], collection[lesserChild] = collection[lesserChild], collection[index]
                index = lesserChild
            return minimum

        def insertHeap(collection, val):
            collection.append(val)
            pos = len(collection) - 1
            while pos > 0:
                parentIdx = (pos - 1) // 2
                if collection[parentIdx] <= collection[pos]:
                    break
                collection[parentIdx], collection[pos] = collection[pos], collection[parentIdx]
                pos = parentIdx

        rebuildHeap(nums)
        countOps = 0

        while True:
            if len(nums) <= 1:
                break
            if nums[0] >= k:
                break
            valA = extractMin(nums)
            valB = extractMin(nums)
            minVal = valA if valA < valB else valB
            maxVal = valA if valA > valB else valB
            combinedVal = (minVal * 2) + maxVal
            insertHeap(nums, combinedVal)
            countOps += 1

        return countOps