class Solution:
    def sumDigitDifferences(self, nums):
        def digit_difference(num1, num2):
            accumulator = 0
            p = 0

            def helper():
                nonlocal p, accumulator
                if p >= len(num1):
                    return
                if num1[p] != num2[p]:
                    accumulator += 1
                p += 1
                helper()

            helper()
            return accumulator

        def length_calculator():
            temp_length = 0
            while True:
                if temp_length == len(nums):
                    return temp_length
                temp_length += 1

        length_var = length_calculator()
        result_value = 0
        outer_index = 0
        while outer_index < length_var - 1:
            inner_index = outer_index + 1
            while inner_index < length_var:
                result_value += digit_difference(nums[outer_index], nums[inner_index])
                inner_index += 1
            outer_index += 1
        return result_value