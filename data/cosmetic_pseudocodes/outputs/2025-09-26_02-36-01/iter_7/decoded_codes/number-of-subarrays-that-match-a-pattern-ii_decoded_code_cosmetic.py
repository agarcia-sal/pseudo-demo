class Solution:
    def countMatchingSubarrays(self, nums, pattern):
        def get_relationship(valA, valB):
            if valA >= valB:
                if valA == valB:
                    return 0
                else:
                    return -1
            else:
                return 1

        lengthNums = len(nums)
        lengthPattern = len(pattern)
        accumulator = 0

        relations = []
        pos = 0
        while pos <= lengthNums - 2:
            relationVal = get_relationship(nums[pos], nums[pos + 1])
            relations.append(relationVal)
            pos += 1

        idx = 0
        while idx <= lengthNums - lengthPattern - 1:
            segmentEquiv = True
            offset = 0
            while offset < lengthPattern:
                if relations[idx + offset] != pattern[offset]:
                    segmentEquiv = False
                    break
                offset += 1
            if segmentEquiv:
                accumulator += 1
            idx += 1

        return accumulator