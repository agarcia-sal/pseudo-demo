class Solution:
    def maxSubarraySum(self, nums):
        def kadane(array):
            current_max = global_max = array[0]
            for i in range(1, len(array)):
                current_max = max(array[i], current_max + array[i])
                global_max = max(global_max, current_max)
            return global_max

        max_sum = kadane(nums)
        distinct_values = set(nums)

        for val in distinct_values:
            filtered_list = [element for element in nums if element != val]
            if filtered_list:
                current_kadane_result = kadane(filtered_list)
                if current_kadane_result > max_sum:
                    max_sum = current_kadane_result

        return max_sum