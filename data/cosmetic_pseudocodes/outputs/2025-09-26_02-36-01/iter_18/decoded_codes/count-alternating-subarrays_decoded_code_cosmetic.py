class Solution:
    def countAlternatingSubarrays(self, nums):
        length_var = len(nums)
        if length_var == 0:
            return 0
        accumulator = length_var
        tracker = 1
        index_var = 1
        while index_var < length_var:
            if nums[index_var] != nums[index_var - 1]:
                tracker += 1
            else:
                tracker = 1
            accumulator += tracker - 1
            index_var += 1
        return accumulator