from collections import defaultdict

class Solution:
    def mostFrequentIDs(self, nums, freq):
        def heapPop(h):
            if not h:
                return None
            lastIdx = len(h) - 1
            topElem = h[0]
            h[0] = h[lastIdx]
            h.pop()
            heapifyDown(h, 0)
            return topElem

        def heapPush(h, elem):
            h.append(elem)
            heapifyUp(h, len(h) - 1)

        def heapifyUp(h, idx):
            while idx > 0:
                parent = (idx - 1) // 2
                if h[parent][0] <= h[idx][0]:
                    break
                h[parent], h[idx] = h[idx], h[parent]
                idx = parent

        def heapifyDown(h, idx):
            size = len(h)
            while True:
                left = 2 * idx + 1
                right = 2 * idx + 2
                smallest = idx
                if left < size and h[left][0] < h[smallest][0]:
                    smallest = left
                if right < size and h[right][0] < h[smallest][0]:
                    smallest = right
                if smallest == idx:
                    break
                h[smallest], h[idx] = h[idx], h[smallest]
                idx = smallest

        dictCounter = defaultdict(int)
        heapStorage = []
        outputResult = []

        def processAtIndex(i):
            if i >= len(nums):
                return
            currentNum = nums[i]
            currentFreq = freq[i]
            dictCounter[currentNum] += currentFreq
            heapPush(heapStorage, [-dictCounter[currentNum], currentNum])
            while heapStorage:
                topPair = heapStorage[0]
                negCount = -topPair[0]
                valNum = topPair[1]
                if negCount == dictCounter[valNum]:
                    break
                heapPop(heapStorage)
            if heapStorage:
                outputResult.append(-heapStorage[0][0])
            else:
                outputResult.append(0)
            processAtIndex(i + 1)

        processAtIndex(0)
        return outputResult