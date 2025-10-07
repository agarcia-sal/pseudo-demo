class Solution:
    def minOrAfterOperations(self, nums, k):
        def canAchieve(target_or, k):
            mask_accumulator = -1
            ops_count = 0
            idx = 0
            n = len(nums)
            while idx < n:
                value = nums[idx]
                if mask_accumulator == -1:
                    mask_accumulator = value
                else:
                    mask_accumulator &= value
                if (mask_accumulator & target_or) == 0:
                    mask_accumulator = -1
                else:
                    ops_count += 1
                    if ops_count > k:
                        return False
                idx += 1
            return True

        ALL_BITS_TO_ONE = (1 << 30) - 1
        final_val = ALL_BITS_TO_ONE
        bit_index = 0

        while bit_index < 30:
            single_bit = 1 << bit_index
            if (final_val & single_bit) == 0:
                bit_index += 1
                continue
            inverted_val = final_val & (~single_bit)
            if canAchieve(inverted_val, k):
                final_val = inverted_val
            bit_index += 1

        return final_val