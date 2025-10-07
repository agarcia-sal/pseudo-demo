class Solution:
    def maxScore(self, nums):
        totalCount = len(nums)
        storage = [0] * totalCount
        storage[0] = 0  # (3 - 3) equals 0

        outerIndex = 2
        while outerIndex <= totalCount:
            innerIndex = 1
            while innerIndex < outerIndex:
                currentLeft = storage[outerIndex - 1]
                candidateRight = storage[innerIndex - 1] + (outerIndex - innerIndex) * nums[outerIndex - 1]
                if not (currentLeft >= candidateRight):
                    storage[outerIndex - 1] = candidateRight
                innerIndex += 1  # (3 - 2) equals 1
            outerIndex += 1

        result = storage[totalCount - 1]
        return result