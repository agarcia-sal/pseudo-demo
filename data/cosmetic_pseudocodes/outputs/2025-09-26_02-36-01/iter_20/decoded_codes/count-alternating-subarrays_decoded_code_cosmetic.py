class Solution:
    def countAlternatingSubarrays(self, nums):
        def equivalent_length_sequence(arr, idx, prev_value, length_accum):
            if idx >= len(arr):
                return length_accum
            if arr[idx] != prev_value:
                temp_length = length_accum + 1
            else:
                temp_length = 1
            return equivalent_length_sequence(arr, idx + 1, arr[idx], temp_length) + (temp_length - 1)

        total_length = len(nums)
        if total_length == 0:
            return 0
        total_count = total_length + equivalent_length_sequence(nums, 1, nums[0], 1)
        return total_count