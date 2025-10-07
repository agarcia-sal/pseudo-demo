class Solution:
    def canSortArray(self, nums):
        def count_set_bits(n):
            def bit_counter(x):
                counter = 0
                while x != 0:
                    if x % 2 == 1:
                        counter += 1
                    x //= 2
                return counter
            return bit_counter(n)

        length_nums = len(nums)
        ordered_nums = [nums[k] for k in range(length_nums)]
        ordered_nums.sort()

        index_i = 0
        while index_i <= length_nums - 1:
            index_j = 0
            while index_j <= length_nums - 2:
                first_val = nums[index_j]
                second_val = nums[index_j + 1]

                first_bits = count_set_bits(first_val)
                second_bits = count_set_bits(second_val)

                if first_bits != second_bits:
                    condition_met = False
                else:
                    condition_met = first_val > second_val

                if condition_met:
                    nums[index_j], nums[index_j + 1] = second_val, first_val

                index_j += 1
            index_i += 1

        are_equal = True
        compare_idx = 0
        while compare_idx < length_nums and are_equal:
            if nums[compare_idx] != ordered_nums[compare_idx]:
                are_equal = False
            compare_idx += 1

        return are_equal