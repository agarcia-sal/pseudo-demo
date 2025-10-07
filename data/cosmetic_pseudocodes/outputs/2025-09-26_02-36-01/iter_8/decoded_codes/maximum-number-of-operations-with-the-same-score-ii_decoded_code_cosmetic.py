class Solution:
    def maxOperations(self, nums):
        def dfs(x, y, accu, cache):
            if x >= y:
                return 0
            if (x, y, accu) in cache:
                return cache[(x, y, accu)]
            tally = 0
            if nums[x] + nums[x + 1] == accu:
                left_val = dfs(x + 2, y, accu, cache)
                tally = max(tally, 1 + left_val)
            if nums[y] + nums[y - 1] == accu:
                right_val = dfs(x, y - 1, accu, cache)
                tally = max(tally, 1 + right_val)
            if nums[x] + nums[y] == accu:
                cross_val = dfs(x + 1, y - 1, accu, cache)
                tally = max(tally, 1 + cross_val)
            cache[(x, y, accu)] = tally
            return tally

        first_case = 1 + dfs(2, len(nums) - 2, nums[0] + nums[1], {})
        second_case = 1 + dfs(0, len(nums) - 3, nums[len(nums) - 2] + nums[len(nums) - 1], {})
        third_case = 1 + dfs(1, len(nums) - 3, nums[0] + nums[len(nums) - 1], {})

        return max(first_case, second_case, third_case)