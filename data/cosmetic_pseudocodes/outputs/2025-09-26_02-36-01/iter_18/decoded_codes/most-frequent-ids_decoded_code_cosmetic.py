import heapq
from collections import defaultdict

class Solution:
    def mostFrequentIDs(self, nums, freq):
        freqMap = defaultdict(int)
        heapList = []
        outputList = []

        for valA, valB in zip(nums, freq):
            freqMap[valA] += valB
            heapq.heappush(heapList, (-freqMap[valA], valA))

            while heapList:
                topNegFreq, topNum = heapList[0]
                if -topNegFreq != freqMap[topNum]:
                    heapq.heappop(heapList)
                else:
                    break

            tempResult = 0
            if heapList:
                tempResult = -heapList[0][0]

            outputList.append(tempResult)

        return outputList