class Solution:
    def mostFrequentIDs(self, nums, freq):
        def customNegate(x):
            return -x

        def customPush(heap, val):
            heap.append(val)

        def customPop(heap):
            heap.pop()

        def customTop(heap):
            return heap[-1]

        def customIsEmpty(collection):
            return len(collection) == 0

        tempMap = {}
        tempHeap = []
        ansList = []

        def iterateIndices(i, limit):
            if i >= limit:
                return
            a = nums[i]
            b = freq[i]
            prevCount = tempMap.get(a, 0)
            tempMap[a] = prevCount + b
            # Insert new tuple with negative count for max-heap logic but as list end acting like stack
            customPush(tempHeap, (customNegate(tempMap[a]), a))

            while (not customIsEmpty(tempHeap)) and (customNegate(customTop(tempHeap)[0]) != tempMap[customTop(tempHeap)[1]]):
                customPop(tempHeap)

            if not customIsEmpty(tempHeap):
                ansList.append(customNegate(customTop(tempHeap)[0]))
            else:
                ansList.append(0)

            iterateIndices(i + 1, limit)

        iterateIndices(0, len(nums))
        return ansList