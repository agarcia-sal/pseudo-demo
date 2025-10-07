class Solution:
    def maxOperations(self, nums):
        def probe(x, y, z, cache):
            if x >= y:
                return 0
            key = (x, y, z)
            if key in cache:
                return cache[key]
            greatest = 0
            if nums[x] + nums[x + 1] == z:
                candidate = 1 + probe(x + 2, y, z, cache)
                if candidate > greatest:
                    greatest = candidate
            if nums[y] + nums[y - 1] == z:
                candidate = 1 + probe(x, y - 2, z, cache)
                if candidate > greatest:
                    greatest = candidate
            if nums[x] + nums[y] == z:
                candidate = 1 + probe(x + 1, y - 1, z, cache)
                if candidate > greatest:
                    greatest = candidate
            cache[key] = greatest
            return greatest

        n = len(nums)
        result1 = 1 + probe(2, n - 1, nums[0] + nums[1], {})
        result2 = 1 + probe(0, n - 3, nums[n - 2] + nums[n - 1], {})
        result3 = 1 + probe(1, n - 2, nums[0] + nums[n - 1], {})
        return max(result1, result2, result3)