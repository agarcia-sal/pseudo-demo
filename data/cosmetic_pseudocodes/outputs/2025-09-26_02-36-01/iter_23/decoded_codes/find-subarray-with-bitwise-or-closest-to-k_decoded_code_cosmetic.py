from math import inf

class Solution:
    def minimumDifference(self, nums, k):
        sz = len(nums)
        retVal = inf

        pos1 = 0
        while pos1 <= sz - 1:
            temp_or = 0
            pos2 = pos1
            while pos2 <= sz - 1:
                temp_or |= nums[pos2]
                delta = (k - temp_or) if k >= temp_or else (temp_or - k) * -1
                if delta < retVal:
                    retVal = delta
                if delta == 0:
                    return retVal
                pos2 += 1
            pos1 += 1

        return retVal