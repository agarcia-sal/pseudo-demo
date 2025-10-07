class Solution:
    def canSortArray(self, nums):
        def tally_bits(value):
            accumulator = 0
            while value != 0:
                accumulator += value & 1
                value >>= 1
            return accumulator

        total = len(nums)
        ordered_list = [nums[i] for i in range(total)]

        def simple_sort(array):
            changed = True
            while changed:
                changed = False
                for k in range(len(array) - 1):
                    if tally_bits(array[k]) == tally_bits(array[k + 1]) and array[k] > array[k + 1]:
                        array[k], array[k + 1] = array[k + 1], array[k]
                        changed = True
            return array

        sorted_copy = simple_sort(ordered_list)

        if len(nums) != len(sorted_copy):
            return False
        for pos in range(total):
            if nums[pos] != sorted_copy[pos]:
                return False
        return True