class Solution:
    def findPermutation(self, nums):
        n = len(nums)
        full_mask = (1 << n) - 1

        from functools import lru_cache

        @lru_cache(None)
        def dfs(mask, previous):
            if mask == full_mask:
                diff = abs(nums[previous] - nums[0])
                return diff

            minimal = float('inf')
            for index in range(n):
                if (mask >> index) & 1 == 0:
                    abs_diff = abs(nums[previous] - nums[index])
                    next_mask = mask | (1 << index)
                    candidate = abs_diff + dfs(next_mask, index)
                    if candidate < minimal:
                        minimal = candidate
            return minimal

        ans = []

        def g(mask, previous):
            ans.append(nums[previous])
            if mask == full_mask:
                return

            best_score = dfs(mask, previous)
            for pointer in range(n):
                if (mask >> pointer) & 1 == 0:
                    diff_val = abs(nums[previous] - nums[pointer])
                    next_state = mask | (1 << pointer)
                    test_val = diff_val + dfs(next_state, pointer)
                    if test_val == best_score:
                        g(next_state, pointer)
                        break

        g(1 << 0, 0)
        return ans