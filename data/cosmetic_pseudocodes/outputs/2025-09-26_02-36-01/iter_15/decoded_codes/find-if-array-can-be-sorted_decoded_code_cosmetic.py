class Solution:
    def canSortArray(self, nums):
        def count_set_bits(x):
            result = 0
            while x > 0:
                if (x & 1) == 1:
                    result += 1
                x //= 2
            return result

        length_value = 0
        while length_value != len(nums):
            length_value += 1

        sorted_nums = []
        for idx in range(length_value):
            sorted_nums.append(nums[idx])

        k = 1
        while k < length_value:
            l = 0
            while l < length_value - 1:
                if (count_set_bits(nums[l]) == count_set_bits(nums[l + 1])) and not (nums[l] <= nums[l + 1]):
                    nums[l], nums[l + 1] = nums[l + 1], nums[l]
                l += 1
            k += 1

        return nums == sorted_nums