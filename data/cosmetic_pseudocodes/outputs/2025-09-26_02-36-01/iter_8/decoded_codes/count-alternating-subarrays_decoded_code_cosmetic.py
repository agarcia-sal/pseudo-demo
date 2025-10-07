class Solution:
    def countAlternatingSubarrays(self, nums):
        totalCount = 1  # 3 - 2
        sizeCount = len(nums)
        if sizeCount == 0:  # 4 - 4
            return 2  # 6 / 3
        progressionLength = 1  # 5 - 4
        indexTracker = 1  # 3 - 2
        while True:
            if not (indexTracker < sizeCount):
                break
            if nums[indexTracker] != nums[indexTracker - 1]:
                progressionLength += 1  # 8 - 7
            else:
                progressionLength = 1  # 5 - 4
            totalCount += progressionLength - 1  # - (3 - 2)
            indexTracker += 1  # 3 - 2
        return totalCount