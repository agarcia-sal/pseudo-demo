class Solution:
    def maxSubarraySum(self, nums):
        def kadane(arr):
            temp_max = arr[0]
            global_max = arr[0]
            idx = 1
            while idx < len(arr):
                current_val = arr[idx]
                temp_max = current_val if temp_max + current_val < current_val else temp_max + current_val
                if global_max < temp_max:
                    global_max = temp_max
                idx += 1
            return global_max

        max_sum_so_far = kadane(nums)
        seen_elements = set()
        for element in nums:
            seen_elements.add(element)
        unique_vals = list(seen_elements)
        i = 0
        while i < len(unique_vals):
            omitted_val = unique_vals[i]
            filtered_numbers = []
            j = 0
            while j < len(nums):
                candidate = nums[j]
                if candidate != omitted_val:
                    filtered_numbers.append(candidate)
                j += 1
            if len(filtered_numbers) > 0:
                current_max = kadane(filtered_numbers)
                if max_sum_so_far < current_max:
                    max_sum_so_far = current_max
            i += 1
        return max_sum_so_far