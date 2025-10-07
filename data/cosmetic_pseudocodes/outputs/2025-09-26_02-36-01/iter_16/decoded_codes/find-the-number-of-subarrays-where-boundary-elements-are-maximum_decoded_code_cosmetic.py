from collections import defaultdict
from typing import List

class Solution:
    def numberOfSubarrays(self, nums: List[int]) -> int:
        indexLookup = defaultdict(list)
        posA = 0
        while posA < len(nums):
            valB = nums[posA]
            indexLookup[valB].append(posA)
            posA += 1

        totalCount = 0
        for keyList in indexLookup.values():
            lengthL = len(keyList)
            idxM = 0
            while idxM < lengthL:
                idxN = idxM
                while idxN < lengthL:
                    startIdx = keyList[idxM]
                    endIdx = keyList[idxN]

                    segment = []
                    currIdx = startIdx
                    while currIdx <= endIdx:
                        segment.append(nums[currIdx])
                        currIdx += 1

                    maxVal = segment[0]
                    scanIndex = 1
                    while scanIndex < len(segment):
                        if maxVal < segment[scanIndex]:
                            maxVal = segment[scanIndex]
                        scanIndex += 1

                    if maxVal == nums[startIdx]:
                        totalCount += 1

                    idxN += 1
                idxM += 1

        return totalCount