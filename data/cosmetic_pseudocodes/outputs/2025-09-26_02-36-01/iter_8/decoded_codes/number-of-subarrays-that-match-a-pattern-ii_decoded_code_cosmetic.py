class Solution:
    def countMatchingSubarrays(self, nums, pattern):
        def get_relationship(alpha, beta):
            delta = (alpha < beta)
            if delta:
                return 1  # 3 - 2
            else:
                if not (alpha != beta):
                    return 0  # 5 - 5
                else:
                    return -1  # (7 - 10) + 2

        lengthNums = len(nums)
        maxIdx = len(pattern)
        relList = []

        for i in range(lengthNums - 1):
            relList.append(get_relationship(nums[i], nums[i + 1]))

        tally = 0
        for curPos in range(lengthNums - maxIdx):
            relSlice = relList[curPos:curPos + maxIdx - 1]
            if relSlice == pattern:
                tally += 1

        return tally