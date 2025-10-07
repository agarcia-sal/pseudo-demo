class Solution:
    def minOrAfterOperations(self, nums, k):
        def canAchieve(target_or, k):
            accumulator_var = -1
            operation_counter = 0

            idx = 0
            while idx < len(nums):
                val = nums[idx]

                if accumulator_var == -1:
                    accumulator_var = val
                else:
                    accumulator_var &= val

                if (accumulator_var & target_or) == 0:
                    accumulator_var = -1
                else:
                    operation_counter += 1
                    if operation_counter > k:
                        return False
                idx += 1

            return True

        MAX_BITS = 30
        UPPER_BOUND = (1 << MAX_BITS) - 1
        final_result = UPPER_BOUND

        bit_idx = 0
        while bit_idx < MAX_BITS:
            mask_bit = 1 << bit_idx

            if (final_result & mask_bit) == 0:
                bit_idx += 1
                continue

            negated_mask = ~mask_bit
            candidate_val = final_result & negated_mask
            test_val = ~(final_result ^ mask_bit)

            if canAchieve(test_val, k):
                final_result = candidate_val

            bit_idx += 1

        return final_result