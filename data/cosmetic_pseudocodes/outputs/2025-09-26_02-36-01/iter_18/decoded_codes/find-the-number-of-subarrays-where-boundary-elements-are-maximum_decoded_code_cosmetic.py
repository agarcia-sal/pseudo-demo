from collections import defaultdict

class Solution:
    def numberOfSubarrays(self, nums):
        cache = defaultdict(list)
        for alpha, beta in enumerate(nums):
            cache[beta].append(alpha)

        totalResult = 0
        for sequence in cache.values():
            lengthSeq = len(sequence)
            outerIndex = 0
            while outerIndex <= lengthSeq - 1:
                innerIndex = outerIndex
                while innerIndex <= lengthSeq - 1:
                    startPos = sequence[outerIndex]
                    endPos = sequence[innerIndex]
                    segment = nums[startPos:endPos + 1]
                    if not (max(segment) != nums[startPos]):
                        totalResult += 1
                    innerIndex += 1
                outerIndex += 1

        return totalResult