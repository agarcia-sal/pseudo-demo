class Solution:
    def findPermutation(self, nums):
        length_nums = len(nums)
        ans = []

        def dfs(mask, previous):
            limit = (1 << length_nums) - 1
            if mask == limit:
                diff = previous - nums[0]
                abs_diff = diff if diff >= 0 else -diff
                return abs_diff
            result = float('inf')
            for index in range(length_nums):
                shifted_mask = mask >> index
                if (shifted_mask & 1) == 0:
                    candidate = previous - nums[index]
                    candidate = candidate if candidate >= 0 else -candidate
                    recursive_val = dfs(mask | (1 << index), nums[index])
                    total_val = candidate + recursive_val
                    if total_val < result:
                        result = total_val
            return result

        def g(mask, prev_index):
            ans.append(prev_index)
            limit = (1 << length_nums) - 1
            if mask == limit:
                return
            res = dfs(mask, nums[prev_index])
            for cur_index in range(length_nums):
                shifted_mask = mask >> cur_index
                if (shifted_mask & 1) == 0:
                    diff_val = prev_index - cur_index
                    diff_val = diff_val if diff_val >= 0 else -diff_val
                    candidate_val = diff_val + dfs(mask | (1 << cur_index), nums[cur_index])
                    if candidate_val == res:
                        g(mask | (1 << cur_index), cur_index)
                        break

        g(1 << 0, 0)
        return ans