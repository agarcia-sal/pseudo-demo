class Solution:
    def maxOperations(self, nums):
        def helper(x, y, threshold, cache):
            if not (x < y):
                return 0
            if (x, y, threshold) in cache:
                return cache[(x, y, threshold)]

            best_count = 0
            if nums[x] + nums[x + 1] == threshold:
                candidate1 = 1 + helper(x + 2, y, threshold, cache)
                if candidate1 > best_count:
                    best_count = candidate1
            if nums[y] + nums[y - 1] == threshold:
                candidate2 = 1 + helper(x, y - 2, threshold, cache)
                if candidate2 > best_count:
                    best_count = candidate2
            if nums[x] + nums[y] == threshold:
                candidate3 = 1 + helper(x + 1, y - 1, threshold, cache)
                if candidate3 > best_count:
                    best_count = candidate3

            cache[(x, y, threshold)] = best_count
            return best_count

        start_1 = 1 + helper(2, len(nums) - 1, nums[0] + nums[1], {})
        start_2 = 1 + helper(0, len(nums) - 3, nums[-2] + nums[-1], {})
        start_3 = 1 + helper(1, len(nums) - 2, nums[0] + nums[-1], {})

        return max(start_1, start_2, start_3)