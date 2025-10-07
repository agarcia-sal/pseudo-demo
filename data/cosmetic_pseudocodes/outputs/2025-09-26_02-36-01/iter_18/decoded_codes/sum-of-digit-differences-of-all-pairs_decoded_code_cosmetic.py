class Solution:
    def sumDigitDifferences(self, nums):
        def sliceDelta(a, b):
            tally = 0
            pos = 0
            while pos < len(a):
                if a[pos] != b[pos]:
                    tally += 1
                pos += 1
            return tally

        accumulator = 0
        limit = len(nums)
        outerIndex = 0

        while True:
            if outerIndex >= limit:
                break
            innerIndex = outerIndex + 1

            while innerIndex < limit:
                accumulator += sliceDelta(nums[outerIndex], nums[innerIndex])
                innerIndex += 1

            outerIndex += 1

        return accumulator