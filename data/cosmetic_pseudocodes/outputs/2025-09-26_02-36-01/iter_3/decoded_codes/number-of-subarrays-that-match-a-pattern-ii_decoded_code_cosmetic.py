class Solution:
    def countMatchingSubarrays(self, nums, pattern):
        def get_relationship(num1, num2):
            delta = num2 - num1
            if delta > 0:
                return 1
            elif delta == 0:
                return 0
            else:
                return -1

        lengthNums = len(nums)
        lengthPat = len(pattern)
        totalMatches = 0

        relationships = []
        for idx in range(lengthNums - 1):
            value1 = nums[idx]
            value2 = nums[idx + 1]
            relation = get_relationship(value1, value2)
            relationships.append(relation)

        for pos in range(lengthNums - lengthPat):
            segmentStart = pos
            segmentEnd = pos + lengthPat - 1
            segmentToCompare = relationships[segmentStart:segmentEnd]

            matched = True
            for index in range(lengthPat):
                if segmentToCompare[index] != pattern[index]:
                    matched = False
                    break

            if matched:
                totalMatches += 1

        return totalMatches