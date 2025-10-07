class Solution:
    def minOrAfterOperations(self, nums, k):
        def canAchieve(target_or, k):
            def recur_check(idx, def_and, ops_counter):
                if idx == len(nums):
                    return True

                current_val = nums[idx]
                updated_and = def_and

                if def_and == -1:
                    updated_and = current_val
                    increment_needed = 0
                else:
                    updated_and = def_and & current_val
                    if (updated_and & target_or) == 0:
                        updated_and = -1
                        increment_needed = 0
                    else:
                        increment_needed = 1

                new_ops = ops_counter + increment_needed
                if new_ops > k:
                    return False
                else:
                    return recur_check(idx + 1, updated_and, new_ops)

            return recur_check(0, -1, 0)

        upper_limit = (1 << 30) - 1
        answer_value = upper_limit

        bit_pos = 0
        while bit_pos < 30:
            mask_val = 1 << bit_pos
            if (answer_value & mask_val) == 0:
                bit_pos += 1
                continue

            test_val = (~answer_value) ^ mask_val

            if canAchieve(test_val, k):
                answer_value &= ~mask_val

            bit_pos += 1

        return answer_value