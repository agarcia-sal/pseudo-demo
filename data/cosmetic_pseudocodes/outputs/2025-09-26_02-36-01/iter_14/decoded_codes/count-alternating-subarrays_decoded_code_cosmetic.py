class Solution:
    def countAlternatingSubarrays(self, nums: list[int]) -> int:
        total_elements = len(nums)
        if total_elements == 0:
            return 0
        total_subarrays = total_elements
        sequence_length = 1
        index_tracker = 1  # zero-based indexing in Python
        while index_tracker < total_elements:
            if nums[index_tracker] != nums[index_tracker - 1]:
                sequence_length += 1
            else:
                sequence_length = 1
            total_subarrays += sequence_length - 1
            index_tracker += 1
        return total_subarrays