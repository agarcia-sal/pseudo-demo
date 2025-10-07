class Solution:
    def canSortArray(self, nums):
        def count_set_bits(number):
            bit_count = 0
            temp_num = number
            while temp_num > 0:
                bit_count += temp_num % 2
                temp_num //= 2
            return bit_count

        length_nums = len(nums)
        sorted_list = sorted(nums)

        index_outer = 0
        while index_outer < length_nums:
            index_inner = 0
            while index_inner < length_nums - 1:
                bits_current = count_set_bits(nums[index_inner])
                bits_next = count_set_bits(nums[index_inner + 1])
                if bits_current == bits_next:
                    if not (nums[index_inner] <= nums[index_inner + 1]):
                        nums[index_inner], nums[index_inner + 1] = nums[index_inner + 1], nums[index_inner]
                index_inner += 1
            index_outer += 1

        is_equal = True
        check_index = 0
        while check_index < length_nums and is_equal:
            if nums[check_index] != sorted_list[check_index]:
                is_equal = False
            check_index += 1

        return is_equal