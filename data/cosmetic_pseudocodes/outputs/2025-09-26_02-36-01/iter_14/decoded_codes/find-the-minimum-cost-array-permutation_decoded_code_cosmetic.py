class Solution:
    def findPermutation(self, nums):
        n = len(nums)
        full_mask = (1 << n) - 1
        from functools import lru_cache

        @lru_cache(None)
        def explore(current_mask, prev_idx):
            if current_mask == full_mask:
                return abs(nums[prev_idx] - nums[0])
            min_result = float("inf")
            for i in range(n):
                if (current_mask >> i) & 1 == 0:
                    temp_calc = abs(nums[prev_idx] - nums[i]) + explore(current_mask | (1 << i), i)
                    if temp_calc < min_result:
                        min_result = temp_calc
            return min_result

        ans = []

        def buildSolution(accum_mask, last_idx):
            ans.append(last_idx)
            if accum_mask == full_mask:
                return
            target = explore(accum_mask, last_idx)
            for i in range(n):
                if (accum_mask >> i) & 1 == 0:
                    candidate_score = abs(nums[last_idx] - nums[i]) + explore(accum_mask | (1 << i), i)
                    if candidate_score == target:
                        buildSolution(accum_mask | (1 << i), i)
                        break

        buildSolution(1 << 0, 0)
        return ans