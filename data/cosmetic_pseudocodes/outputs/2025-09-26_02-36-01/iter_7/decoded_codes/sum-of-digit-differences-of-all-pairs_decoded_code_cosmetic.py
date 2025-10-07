class Solution:
    def sumDigitDifferences(self, nums):
        def digit_difference(num1, num2):
            accumulator = 0
            position = 0
            length = len(num1)
            while position < length:
                if num1[position] != num2[position]:
                    accumulator += 1
                position += 1
            return accumulator

        result = 0
        length_nums = len(nums)
        outer_index = 0

        while True:
            if outer_index >= length_nums:
                break

            inner_index = length_nums - 1

            while True:
                if inner_index <= outer_index:
                    break

                first_element = nums[outer_index]
                second_element = nums[inner_index]
                delta = digit_difference(first_element, second_element)
                result += delta
                inner_index -= 1

            outer_index += 1

        return result