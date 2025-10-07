class Solution:
    def sumDigitDifferences(self, nums):
        def digit_difference(num1, num2):
            def recursive_check(pos):
                if pos == len(num1):
                    return 0
                current_diff = 0 if num1[pos] == num2[pos] else 1
                return current_diff + recursive_check(pos + 1)
            return recursive_check(0)

        output = 0
        length_nums = len(nums)
        outer_index = 0
        while outer_index < length_nums - 1:
            inner_index = outer_index + 1
            while inner_index < length_nums:
                output += digit_difference(nums[outer_index], nums[inner_index])
                inner_index += 1
            outer_index += 1
        return output