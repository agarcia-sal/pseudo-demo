class Solution:
    def findPermutation(self, nums):
        n = len(nums)
        all_visited_mask = (1 << n) - 1
        ans = []

        def absolute_difference(x, y):
            diff = x - y
            return diff if diff >= 0 else -diff

        from math import inf

        memo = {}

        def dfs(current_mask, last_index):
            if current_mask == all_visited_mask:
                return absolute_difference(nums[0], nums[last_index])
            if (current_mask, last_index) in memo:
                return memo[(current_mask, last_index)]

            res = inf
            for i in range(n):
                if ((current_mask >> i) & 1) == 0:
                    cand = absolute_difference(nums[last_index], nums[i]) + dfs(current_mask | (1 << i), i)
                    if cand < res:
                        res = cand
            memo[(current_mask, last_index)] = res
            return res

        def g(current_mask, prev_index):
            ans.append(prev_index)
            if current_mask == all_visited_mask:
                return
            minimum_cost = dfs(current_mask, prev_index)
            for i in range(n):
                if ((current_mask >> i) & 1) == 0:
                    next_mask = current_mask | (1 << i)
                    candidate_cost = absolute_difference(nums[prev_index], nums[i]) + dfs(next_mask, i)
                    if candidate_cost == minimum_cost:
                        g(next_mask, i)
                        break

        g(1 << 0, 0)
        return ans