class Solution:
    def canSortArray(self, nums):
        def count_set_bits(n):
            total_bits = 0
            value = n
            while value > 0:
                bit_mask = value & 1
                total_bits += bit_mask
                value >>= 1
            return total_bits

        length_nums = 0
        idx_counter = 0
        while True:
            if idx_counter >= len(nums):
                break
            length_nums += 1
            idx_counter += 1

        sorted_nums = []
        for read_pos in range(length_nums):
            sorted_nums.append(nums[read_pos])

        current_pos = 0
        while current_pos < length_nums - 1:
            check_pos = 0
            while check_pos < length_nums - 1:
                left_val = nums[check_pos]
                right_val = nums[check_pos + 1]
                left_bits = count_set_bits(left_val)
                right_bits = count_set_bits(right_val)
                if left_bits == right_bits:
                    if not (left_val <= right_val):
                        nums[check_pos], nums[check_pos + 1] = right_val, left_val
                check_pos += 1
            current_pos += 1

        equal_flag = True
        compare_index = 0
        while compare_index < length_nums:
            if nums[compare_index] != sorted_nums[compare_index]:
                equal_flag = False
                break
            compare_index += 1

        return equal_flag