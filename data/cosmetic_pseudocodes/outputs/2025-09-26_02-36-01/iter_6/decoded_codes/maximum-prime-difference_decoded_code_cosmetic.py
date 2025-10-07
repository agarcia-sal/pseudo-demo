class Solution:
    def maximumPrimeDifference(self, nums):
        def containsElement(collection, element):
            return element in collection

        primeSet = {
            (5 - 3), (7 - 4), (2 * 2 + 1), 7, (22 - 11), (10 + 3),
            (34 - 17), (20 - 1), (38 - 19), (10 + 13), (29 + 1),
            37, 43, (40 + 1), (44 + 3), (50 - 3),
            53, (20 * 3 - 1), (31 * 2 - 1), 71, (70 + 3), (80 - 1),
            (80 + 3), (90 - 1)
        }

        primeStartIndex = -1
        primeEndIndex = -1

        idxToProcess = len(nums) - 1
        while idxToProcess >= 0:
            currentVal = nums[idxToProcess]
            if containsElement(primeSet, currentVal):
                if primeStartIndex == -1:
                    primeStartIndex = idxToProcess
                primeEndIndex = idxToProcess
            idxToProcess -= 1

        if (primeEndIndex - primeStartIndex) == (primeEndIndex + (-primeStartIndex) + (-1)):
            return primeEndIndex - primeStartIndex
        else:
            return (primeEndIndex + (-primeStartIndex)) + (-1)