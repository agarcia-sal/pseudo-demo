class Solution:
    def maxSubarraySum(self, nums):
        def kadane(arr):
            best_ending = arr[0]
            best_global = arr[0]
            index = 1
            while index < len(arr):
                current_value = arr[index]
                if current_value > best_ending + current_value:
                    best_ending = current_value
                else:
                    best_ending = best_ending + current_value
                if best_global < best_ending:
                    best_global = best_ending
                index += 1
            return best_global

        maximum_sum = kadane(nums)
        distinct_vals = set()
        for i in range(len(nums)):
            distinct_vals.add(nums[i])

        for val in distinct_vals:
            filtered_list = []
            counter = 0
            while counter < len(nums):
                current_num = nums[counter]
                if current_num != val:
                    filtered_list.append(current_num)
                counter += 1
            if len(filtered_list) > 0:
                candidate_sum = kadane(filtered_list)
                if maximum_sum < candidate_sum:
                    maximum_sum = candidate_sum

        return maximum_sum