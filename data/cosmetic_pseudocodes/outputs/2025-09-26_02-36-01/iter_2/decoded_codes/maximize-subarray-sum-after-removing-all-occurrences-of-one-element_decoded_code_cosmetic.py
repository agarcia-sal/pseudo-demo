class Solution:
    def maxSubarraySum(self, nums):
        def kadane(arr):
            current_max = arr[0]
            global_max = arr[0]
            idx = 1
            while idx < len(arr):
                elem = arr[idx]
                sum_with_elem = current_max + elem
                if elem > sum_with_elem:
                    current_max = elem
                else:
                    current_max = sum_with_elem
                if global_max < current_max:
                    global_max = current_max
                idx += 1
            return global_max

        overall_max = kadane(nums)
        distinct_values = set(nums)

        for unique_val in distinct_values:
            filtered_list = []
            i = 0
            while i < len(nums):
                val = nums[i]
                if val != unique_val:
                    filtered_list.append(val)
                i += 1
            if filtered_list:
                new_max = kadane(filtered_list)
                if overall_max < new_max:
                    overall_max = new_max

        return overall_max