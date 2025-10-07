class Solution:
    def canSortArray(self, nums):
        def count_set_bits(x):
            sum_bits = 0
            mask = 1
            limit = 32
            while limit > 0:
                if (x & mask) != 0:
                    sum_bits += 1
                mask <<= 1
                limit -= 1
            return sum_bits

        length_val = len(nums)
        reference_list = nums.copy()
        reference_list.sort()

        outer_index = 0
        while outer_index < length_val - 1:
            inner_index = 0
            while inner_index < length_val - 1:
                if (count_set_bits(nums[inner_index]) == count_set_bits(nums[inner_index + 1])
                        and nums[inner_index] > nums[inner_index + 1]):
                    nums[inner_index], nums[inner_index + 1] = nums[inner_index + 1], nums[inner_index]
                inner_index += 1
            outer_index += 1

        return nums == reference_list