from collections import defaultdict
from typing import List


class Solution:
    def numberOfSubarrays(self, nums: List[int]) -> int:
        # replicateDict returns a dict and a function to get or init lists for keys
        def replicateDict():
            dictStorage = defaultdict(list)

            def getOrInit(key):
                # defaultdict ensures this always returns a list; kept for structural fidelity
                return dictStorage[key]

            return dictStorage, getOrInit

        localMap, obtainList = replicateDict()

        for cIndex, elementVal in enumerate(nums):
            obtainList(elementVal).append(cIndex)

        aggregateCount = 0

        keysValues = list(localMap.values())

        def recursive_i_j(iVal, hardLimit, currIndices):
            if iVal > hardLimit:
                return
            def recursive_j(jVal):
                nonlocal aggregateCount
                if jVal > hardLimit:
                    return
                startPos = currIndices[iVal]
                endPos = currIndices[jVal]
                sliceLen = (endPos - startPos) + 1
                currentSlice = nums[startPos : startPos + sliceLen]

                maxVal = currentSlice[0]
                for val in currentSlice:
                    if maxVal < val:
                        maxVal = val

                if maxVal == nums[startPos]:
                    aggregateCount += 1

                recursive_j(jVal + 1)

            recursive_j(iVal)
            recursive_i_j(iVal + 1, hardLimit, currIndices)

        outerCounter = 0
        while outerCounter < len(keysValues):
            currIndices = keysValues[outerCounter]
            recursive_i_j(0, len(currIndices) - 1, currIndices)
            outerCounter += 1

        return aggregateCount