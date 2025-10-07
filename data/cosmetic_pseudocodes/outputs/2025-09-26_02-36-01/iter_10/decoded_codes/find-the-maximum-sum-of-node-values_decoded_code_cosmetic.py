class Solution:
    def maximumValueSum(self, nums, k, edges):
        accumulator = 0
        counter_positive_diff = 0
        smallest_delta = float('inf')

        def compute_xor(a, b):
            return a ^ b

        def absolute_val(val):
            return -val if val < 0 else val

        def max_val(a, b):
            return a if a > b else b

        def min_val(a, b):
            return a if a < b else b

        def iterate_index(index):
            nonlocal accumulator, counter_positive_diff, smallest_delta
            if index >= len(nums):
                return
            current_num = nums[index]
            computed_xor = compute_xor(current_num, k)
            difference = computed_xor - current_num

            if difference > 0:
                counter_positive_diff += 1

            accumulator += max_val(current_num, computed_xor)
            smallest_delta = min_val(smallest_delta, absolute_val(difference))

            iterate_index(index + 1)

        iterate_index(0)

        if (counter_positive_diff % 2) != 0:
            accumulator -= smallest_delta

        return accumulator