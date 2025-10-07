class Solution:
    def canSortArray(self, nums):
        def count_set_bits(x):
            m = x
            result = 0
            while m > 0:
                result += m & 1
                m >>= 1
            return result

        k = len(nums)
        temp_list = [nums[i] for i in range(k)]
        target = sorted(temp_list)

        for _ in range(k):
            inner_idx = 0
            while inner_idx < k - 1:
                bits_current = count_set_bits(nums[inner_idx])
                bits_next = count_set_bits(nums[inner_idx + 1])
                if bits_current == bits_next and nums[inner_idx] > nums[inner_idx + 1]:
                    nums[inner_idx], nums[inner_idx + 1] = nums[inner_idx + 1], nums[inner_idx]
                inner_idx += 1

        eq_flag = True
        d = 0
        while d < k and eq_flag:
            if nums[d] != target[d]:
                eq_flag = False
            d += 1
        return eq_flag