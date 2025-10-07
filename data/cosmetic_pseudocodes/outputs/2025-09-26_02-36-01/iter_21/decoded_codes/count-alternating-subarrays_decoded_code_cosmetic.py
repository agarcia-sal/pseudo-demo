class Solution:
    def countAlternatingSubarrays(self, nums):
        lengthVar = len(nums)
        resultVar = 0
        if lengthVar == 0:
            return 0
        resultVar = lengthVar
        accumulator = 1
        while accumulator < lengthVar:
            current_length = 1
            while accumulator < lengthVar and nums[accumulator] != nums[accumulator - 1]:
                current_length += 1
                accumulator += 1
            resultVar += (current_length * (current_length - 1)) // 2  # count all subarrays in current alternating segment
            if accumulator < lengthVar and nums[accumulator] == nums[accumulator - 1]:
                accumulator += 1
        return resultVar