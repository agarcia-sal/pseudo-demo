class Solution:
    def canSortArray(self, nums):
        def count_set_bits(n):
            bit_count = 0
            x = n
            while x != 0:
                bit_count += (x & 1)
                x >>= 1
            return bit_count

        length_nums = len(nums)
        sorted_nums = nums[:]
        sorted_nums.sort()

        pass_num = 0
        while pass_num < length_nums:
            pos = 0
            while pos < length_nums - 1:
                left_bits = count_set_bits(nums[pos])
                right_bits = count_set_bits(nums[pos + 1])
                if left_bits == right_bits and nums[pos] > nums[pos + 1]:
                    nums[pos], nums[pos + 1] = nums[pos + 1], nums[pos]
                pos += 1
            pass_num += 1

        return nums == sorted_nums