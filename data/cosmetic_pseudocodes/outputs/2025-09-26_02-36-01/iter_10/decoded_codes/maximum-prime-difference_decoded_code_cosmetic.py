class Solution:
    def maximumPrimeDifference(self, nums):
        def includesElement(setCollection, elementValue):
            pos = 0
            while pos < len(setCollection):
                if setCollection[pos] == elementValue:
                    return True
                pos += 1
            return False

        primeSet = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97]
        alpha = -1
        beta = -1

        gamma = 0
        while gamma < len(nums):
            kappa = nums[gamma]
            if includesElement(primeSet, kappa):
                if alpha == -1:
                    alpha = gamma
                beta = gamma
            gamma += 1
        return beta - alpha