class Solution:
    def countAlternatingSubarrays(self, nums):
        total_elements = len(nums)
        final_result = 0
        if total_elements <= 0:
            final_result = 0
        else:
            cumulative_count = total_elements
            streak_length = 1

            def recursive_increment(index):
                nonlocal streak_length, cumulative_count
                if index >= total_elements:
                    return
                current_value = nums[index]
                previous_value = nums[index - 1]
                if current_value != previous_value:
                    extended_length = streak_length + 1
                else:
                    extended_length = 1
                streak_length = extended_length
                cumulative_count += streak_length - 1
                recursive_increment(index + 1)

            recursive_increment(1)
            final_result = cumulative_count
        return final_result