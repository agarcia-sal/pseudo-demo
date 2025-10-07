class Solution:
    def maximumLength(self, nums):
        def iterate(index, a_even, a_odd):
            if index >= len(nums):
                return a_even, a_odd
            sum_val = nums[index - 1] + nums[index]
            if sum_val % 2 == 0:
                new_even = max(a_even + 1, a_odd)
                return iterate(index + 1, new_even, a_odd)
            else:
                new_odd = max(a_odd + 1, a_even)
                return iterate(index + 1, a_even, new_odd)

        final_even, final_odd = iterate(1, 0, 0)
        return max(final_even, final_odd) + 1