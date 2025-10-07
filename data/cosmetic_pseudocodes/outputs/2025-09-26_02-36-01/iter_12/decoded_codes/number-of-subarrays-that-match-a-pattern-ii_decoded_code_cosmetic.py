class Solution:
    def countMatchingSubarrays(self, nums, pattern):
        def derive_relation(x, y):
            if not (x >= y):
                return 1
            else:
                if x == y:
                    return 0
                else:
                    return -1

        totalNums = len(nums)
        totalPattern = len(pattern)
        tally = 0

        relationVector = []
        posTracker = 0
        while posTracker < totalNums - 1:
            tempRel = derive_relation(nums[posTracker], nums[posTracker + 1])
            relationVector.append(tempRel)
            posTracker += 1

        scanIdx = 0
        while True:
            if scanIdx > (totalNums - totalPattern - 1):
                break

            section = []
            offset = 0
            while offset < totalPattern:
                section.append(relationVector[scanIdx + offset])
                offset += 1

            isEqual = True
            cmpIndex = 0
            while cmpIndex < totalPattern:
                if section[cmpIndex] != pattern[cmpIndex]:
                    isEqual = False
                    break
                cmpIndex += 1

            if isEqual:
                tally += 1

            scanIdx += 1

        return tally