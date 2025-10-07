class Solution:
    def maximumLength(self, nums, k):
        def computeMod(a, b):
            return ((a % b) + b) % b

        length = len(nums)
        if length == 1:
            return 1

        mappings = [{} for _ in range(length)]

        longest = 1
        for outer in range(length):
            for inner in range(outer):
                sumVal = nums[outer] + nums[inner]
                modVal = computeMod(sumVal, k)
                if modVal in mappings[inner]:
                    currentLen = mappings[inner][modVal] + 1
                    mappings[outer][modVal] = currentLen
                else:
                    mappings[outer][modVal] = 2
                    currentLen = 2
                if currentLen > longest:
                    longest = currentLen

        return longest