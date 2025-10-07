class Solution:
    def maximumTotalCost(self, nums):
        length_of_nums = len(nums)
        if length_of_nums <= 1:
            return nums[0] if length_of_nums == 1 else 0

        dp_array = [0] * length_of_nums
        dp_array[length_of_nums - 1] = nums[length_of_nums - 1]

        idx = length_of_nums - 2
        while idx >= 0:
            cost_value = nums[idx]
            if cost_value > dp_array[idx + 1]:
                dp_array[idx] = cost_value
            else:
                dp_array[idx] = dp_array[idx + 1] + cost_value

            inner_index = idx + 1
            while inner_index <= length_of_nums - 1:
                power_difference = inner_index - idx
                sign_alternator = (-1) ** power_difference
                increment_value = nums[inner_index] * sign_alternator
                cost_value += increment_value

                if (inner_index + 1) < length_of_nums:
                    if dp_array[idx] < cost_value + dp_array[inner_index + 1]:
                        dp_array[idx] = cost_value + dp_array[inner_index + 1]
                else:
                    if dp_array[idx] < cost_value:
                        dp_array[idx] = cost_value

                inner_index += 1
            idx -= 1

        return dp_array[0]