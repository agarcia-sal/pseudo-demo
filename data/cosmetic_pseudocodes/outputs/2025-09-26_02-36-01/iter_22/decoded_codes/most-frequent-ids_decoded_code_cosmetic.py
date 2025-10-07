from collections import defaultdict
import heapq

class Solution:
    def mostFrequentIDs(self, nums, freq):
        dictCounter = defaultdict(int)
        heapStorage = []
        outputList = []
        for indexX in range(len(nums)):
            currentNum = nums[indexX]
            currentFreq = freq[indexX]
            dictCounter[currentNum] += currentFreq
            heapq.heappush(heapStorage, (-dictCounter[currentNum], currentNum))
            # Remove outdated heap entries
            while heapStorage and -heapStorage[0][0] != dictCounter[heapStorage[0][1]]:
                heapq.heappop(heapStorage)
            if heapStorage:
                outputList.append(-heapStorage[0][0])
            else:
                outputList.append(0)
        return outputList