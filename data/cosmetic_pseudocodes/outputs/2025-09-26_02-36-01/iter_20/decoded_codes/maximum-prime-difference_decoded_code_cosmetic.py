class Solution:
    def maximumPrimeDifference(self, nums):
        def isMember(setRef, val):
            for idx in range(len(setRef)):
                if setRef[idx] == val:
                    return True
            return False

        alpha = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97]
        beta = -1
        gamma = -1

        def scanAll(current, accFirst, accLast):
            if current == len(nums):
                return (accFirst, accLast)
            val = nums[current]
            if isMember(alpha, val):
                newFirst = accFirst
                if accFirst == -1:
                    newFirst = current
                newLast = current
                return scanAll(current + 1, newFirst, newLast)
            else:
                return scanAll(current + 1, accFirst, accLast)

        beta, gamma = scanAll(0, beta, gamma)
        result = gamma + (-1 * beta)
        return result