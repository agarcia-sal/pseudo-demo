class Solution:
    def canSortArray(self, nums):
        def count_set_bits(x):
            total_ones = 0
            mask = 1
            while mask <= x:
                if x & mask != 0:
                    total_ones += 1
                mask <<= 1
            return total_ones

        length_nums = len(nums)
        sorted_copy = nums[:]
        sorted_copy.sort()

        outer_idx = 0
        while outer_idx < length_nums:
            inner_idx = 0
            while inner_idx < length_nums - 1:
                left_bit_count = count_set_bits(nums[inner_idx])
                right_bit_count = count_set_bits(nums[inner_idx + 1])
                if left_bit_count == right_bit_count and nums[inner_idx] > nums[inner_idx + 1]:
                    nums[inner_idx], nums[inner_idx + 1] = nums[inner_idx + 1], nums[inner_idx]
                inner_idx += 1
            outer_idx += 1

        for i in range(length_nums):
            if nums[i] != sorted_copy[i]:
                return False
        return True