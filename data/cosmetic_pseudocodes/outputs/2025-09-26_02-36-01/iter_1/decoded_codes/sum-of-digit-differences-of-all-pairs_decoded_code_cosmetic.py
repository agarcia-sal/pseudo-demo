class Solution:
    def sumDigitDifferences(self, nums):
        def digit_difference(num1, num2):
            difference_counter = 0
            position = 0
            while position < len(num1):
                if num1[position] != num2[position]:
                    difference_counter += 1
                position += 1
            return difference_counter

        aggregate_sum = 0
        length = len(nums)
        i = 0
        while i < length - 1:
            j = i + 1
            while j < length:
                aggregate_sum += digit_difference(nums[i], nums[j])
                j += 1
            i += 1
        return aggregate_sum