class Solution:
    def sumDigitDifferences(self, nums):
        def digit_difference(numA, numB):
            def recurse_chars(cA, cB, pos):
                if pos < len(cA):
                    increment = 0 if cA[pos] == cB[pos] else 1
                    return increment + recurse_chars(cA, cB, pos + 1)
                else:
                    return 0
            return recurse_chars(str(numA), str(numB), 0)

        accumulated_difference = 0
        total_numbers = len(nums)

        def accumulate_pairs(i, j):
            nonlocal accumulated_difference
            if i >= total_numbers - 1:
                return
            elif j >= total_numbers:
                accumulate_pairs(i + 1, i + 2)
            else:
                accumulated_difference += digit_difference(nums[i], nums[j])
                accumulate_pairs(i, j + 1)

        accumulate_pairs(0, 1)
        return accumulated_difference