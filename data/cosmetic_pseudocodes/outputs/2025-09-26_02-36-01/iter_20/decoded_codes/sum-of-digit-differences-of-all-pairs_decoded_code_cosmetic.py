class Solution:
    def sumDigitDifferences(self, nums):
        def digit_difference(a, b):
            def count_mismatches(x, y, pos, acc):
                if pos >= len(x):
                    return acc
                if x[pos] != y[pos]:
                    return count_mismatches(x, y, pos + 1, acc + 1)
                return count_mismatches(x, y, pos + 1, acc)
            return count_mismatches(a, b, 0, 0)

        sum_accumulator = 0
        len_nums = len(nums)
        outer_idx = 0
        while outer_idx < len_nums:
            inner_idx = outer_idx + 1
            while inner_idx < len_nums:
                sum_accumulator += digit_difference(nums[outer_idx], nums[inner_idx])
                inner_idx += 1
            outer_idx += 1
        return sum_accumulator