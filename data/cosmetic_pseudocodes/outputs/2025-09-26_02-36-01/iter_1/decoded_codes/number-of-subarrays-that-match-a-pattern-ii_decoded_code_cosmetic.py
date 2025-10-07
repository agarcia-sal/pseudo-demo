class Solution:
    def countMatchingSubarrays(self, nums, pattern):
        def compute_relation(a, b):
            if a > b:
                return -1
            elif a == b:
                return 0
            else:
                return 1

        lengthNums = len(nums)
        lengthPattern = len(pattern)
        matchedCount = 0

        relations = []
        for i in range(lengthNums - 1):
            relations.append(compute_relation(nums[i], nums[i + 1]))

        for startIdx in range(lengthNums - lengthPattern):
            segment = relations[startIdx:startIdx + lengthPattern]
            if segment == pattern:
                matchedCount += 1

        return matchedCount