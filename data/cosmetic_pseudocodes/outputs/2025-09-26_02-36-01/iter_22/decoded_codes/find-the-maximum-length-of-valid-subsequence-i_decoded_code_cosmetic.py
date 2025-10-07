class Solution:
    def maximumLength(self, nums):
        iterator_index = 1
        accumulator_even = 0
        accumulator_odd = 0
        while iterator_index < len(nums):
            temp_sum = nums[iterator_index - 1] + nums[iterator_index]
            if temp_sum % 2 != 1:
                accumulator_even = max(accumulator_even + 1, accumulator_odd)
            else:
                accumulator_odd = max(accumulator_odd + 1, accumulator_even)
            iterator_index += 1
        output_value = max(accumulator_even, accumulator_odd) + 1
        return output_value