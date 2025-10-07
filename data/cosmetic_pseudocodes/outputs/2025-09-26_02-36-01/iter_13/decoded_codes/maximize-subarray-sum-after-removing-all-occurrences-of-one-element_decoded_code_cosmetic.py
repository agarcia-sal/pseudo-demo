class Solution:
    def maxSubarraySum(self, nums):
        def kadane(arr):
            result_var = arr[0]
            current_max = arr[0]
            index_var = 1
            while index_var < len(arr):
                temp_var = arr[index_var]
                if current_max + temp_var < temp_var:
                    current_max = temp_var
                else:
                    current_max = current_max + temp_var
                if result_var < current_max:
                    result_var = current_max
                index_var += 1
            return result_var

        accumulator = kadane(nums)
        unique_set = set()
        pos_index = 0
        while pos_index < len(nums):
            unique_set |= {nums[pos_index]}
            pos_index += 1

        def filter_out(value, data_list):
            def helper(input_list, acc_list):
                if len(input_list) == 0:
                    return acc_list
                if input_list[0] != value:
                    acc_list = acc_list + [input_list[0]]
                return helper(input_list[1:], acc_list)
            return helper(data_list, [])

        unique_iterator = list(unique_set)
        current_pos = 0
        while True:
            if current_pos >= len(unique_iterator):
                break
            candidate = unique_iterator[current_pos]
            filtered_list = filter_out(candidate, nums)
            if len(filtered_list) > 0:
                candidate_sum = kadane(filtered_list)
                if accumulator < candidate_sum:
                    accumulator = candidate_sum
            current_pos += 1

        return accumulator