class Solution:
    def findPermutation(self, nums):
        LEN_NUMS = len(nums)
        ONE = 1
        ZERO = 0
        ans = []

        def is_full(mask_val):
            return mask_val == (ONE << (LEN_NUMS - ONE))

        def abs_diff(a, b):
            return a - b if a > b else b - a

        from math import inf

        memo = {}

        def dfs(current_mask, last_element):
            if is_full(current_mask):
                return abs_diff(last_element, nums[0])

            if (current_mask, last_element) in memo:
                return memo[(current_mask, last_element)]

            minimal_result = inf

            def try_index(index):
                nonlocal minimal_result
                if ((current_mask >> index) & ONE) == ZERO:
                    temp_val = abs_diff(last_element, nums[index]) + dfs(current_mask | (ONE << index), index)
                    if temp_val < minimal_result:
                        minimal_result = temp_val

            idx = ZERO
            while idx < LEN_NUMS:
                try_index(idx)
                idx += ONE

            memo[(current_mask, last_element)] = minimal_result
            return minimal_result

        def g(current_mask, last_element):
            ans.append(last_element)
            if is_full(current_mask):
                return

            desired_result = dfs(current_mask, last_element)

            def search_index(index):
                if ((current_mask >> index) & ONE) == ZERO:
                    candidate_val = abs_diff(last_element, nums[index]) + dfs(current_mask | (ONE << index), index)
                    if candidate_val == desired_result:
                        g(current_mask | (ONE << index), index)
                        return True
                return False

            pointer = ZERO
            break_flag = False
            while pointer < LEN_NUMS and not break_flag:
                if search_index(pointer):
                    break_flag = True
                else:
                    pointer += ONE

        g(ONE << ZERO, ZERO)
        return ans