class Solution:
    def countMatchingSubarrays(self, nums, pattern):
        def get_relationship(x, y):
            if y > x:
                return 1
            elif y == x:
                return 0
            else:
                return -1

        lengthNums = len(nums)
        lengthPattern = len(pattern)
        totalMatches = 0
        relList = []

        for idx in range(lengthNums - 1):
            relList.append(get_relationship(nums[idx], nums[idx + 1]))

        pos = 0
        while True:
            if pos > lengthNums - lengthPattern - 1:
                break

            subRel = []
            endPos = pos + lengthPattern - 1
            for k in range(pos, endPos + 1):
                subRel.append(relList[k])

            if subRel == pattern:
                totalMatches += 1

            pos += 1

        return totalMatches