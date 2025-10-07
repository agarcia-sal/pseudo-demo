class Solution:
    def sumDigitDifferences(self, nums):
        def digit_difference(num1, num2):
            diff_counter = 0
            pos = 0
            limit = len(num1)
            while pos < limit:
                d_one = num1[pos]
                d_two = num2[pos]
                if d_one != d_two:
                    diff_counter += 1
                pos += 1
            return diff_counter

        aggregate = 0
        length_of_nums = len(nums)
        outer = 0
        while outer < length_of_nums - 1:
            inner = outer + 1
            while inner < length_of_nums:
                current_diff = digit_difference(nums[outer], nums[inner])
                aggregate += current_diff
                inner += 1
            outer += 1
        return aggregate