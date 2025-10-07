from collections import defaultdict

class Solution:
    def numberOfSubarrays(self, nums):
        mapIndices = defaultdict(list)

        def storeIndices(arr, dict_):
            def iterateKeys(kList, source, idx):
                if idx >= len(source):
                    return
                keyVal = source[idx]
                dict_[keyVal].append(kList[idx])
                iterateKeys(kList, source, idx + 1)
            idxList = list(range(len(arr)))
            iterateKeys(idxList, arr, 0)

        storeIndices(nums, mapIndices)

        totalCount = 0
        for listIndices in mapIndices.values():
            limit = len(listIndices) - 1
            iterator1 = 0
            while iterator1 <= limit:
                iterator2 = iterator1
                while iterator2 <= limit:
                    startPos = listIndices[iterator1]
                    endPos = listIndices[iterator2]
                    currentSubarray = nums[startPos:endPos + 1]
                    maxInSub = currentSubarray[0]
                    idxMax = 1
                    while idxMax < len(currentSubarray):
                        if currentSubarray[idxMax] > maxInSub:
                            maxInSub = currentSubarray[idxMax]
                        idxMax += 1
                    testVal = nums[startPos]
                    if maxInSub == testVal:
                        totalCount += 1
                    iterator2 += 1
                iterator1 += 1

        return totalCount