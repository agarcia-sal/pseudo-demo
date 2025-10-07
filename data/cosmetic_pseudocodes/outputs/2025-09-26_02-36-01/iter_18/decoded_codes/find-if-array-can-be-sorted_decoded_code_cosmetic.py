class Solution:
    def canSortArray(self, nums):
        def count_set_bits(x):
            accumulator = 0
            mask = 1
            while x > 0:
                if x & mask != 0:
                    accumulator += 1
                x = x >> 1  # use right shift for dividing by 2
            return accumulator

        length_val = len(nums)
        sorted_nums = nums[:]

        for index_a in range(1, length_val):
            for index_b in range(1, length_val - index_a + 1):
                first_val_bits = count_set_bits(nums[index_b - 1])
                second_val_bits = count_set_bits(nums[index_b])
                # if NOT (first_val_bits != second_val_bits OR nums[index_b - 1] <= nums[index_b])
                # means if first_val_bits == second_val_bits AND nums[index_b - 1] > nums[index_b]
                if first_val_bits == second_val_bits and nums[index_b - 1] > nums[index_b]:
                    nums[index_b - 1], nums[index_b] = nums[index_b], nums[index_b - 1]

        return nums == sorted_nums