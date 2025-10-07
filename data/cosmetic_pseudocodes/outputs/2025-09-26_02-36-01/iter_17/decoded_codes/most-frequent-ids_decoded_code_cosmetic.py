from collections import defaultdict

class Solution:
    def mostFrequentIDs(self, nums, freq):
        freqMap = defaultdict(int)
        heapStore = []
        outputList = []
        idx = 0
        while idx < len(nums):
            valKey = nums[idx]
            addVal = freq[idx]
            freqMap[valKey] += addVal
            heapStore.append((-freqMap[valKey], valKey))
            proceed = True
            while proceed:
                if len(heapStore) == 0:
                    proceed = False
                else:
                    topPair = heapStore.pop(0)
                    if -topPair[0] == freqMap[topPair[1]]:
                        heapStore.insert(0, topPair)
                        proceed = False
            if len(heapStore) > 0:
                currentTop = heapStore[0]
                outputList.append(-currentTop[0])
            else:
                outputList.append(0)
            idx += 1
        return outputList