class Solution:
    def canSortArray(self, nums):
        def count_set_bits(value):
            count = 0
            test_val = value
            while test_val != 0:
                if test_val & 1 != 0:
                    count += 1
                test_val //= 2
            return count

        length_val = 0
        while length_val < len(nums):
            length_val += 1

        ordered_nums = []
        for index in range(length_val):
            ordered_nums.append(nums[index])

        swapped = True
        while swapped:
            swapped = False
            position = 0
            while position < length_val - 1:
                if count_set_bits(nums[position]) == count_set_bits(nums[position + 1]) and nums[position] > nums[position + 1]:
                    temp_val1 = nums[position]
                    nums[position] = nums[position + 1]
                    nums[position + 1] = temp_val1
                    swapped = True
                position += 1

        index_check = 0
        equal_flag = True
        while equal_flag and index_check < length_val:
            if nums[index_check] != ordered_nums[index_check]:
                equal_flag = False
            index_check += 1

        return equal_flag