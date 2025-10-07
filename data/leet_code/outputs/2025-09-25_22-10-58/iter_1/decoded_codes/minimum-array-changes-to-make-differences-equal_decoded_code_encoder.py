class Solution:
    def minChanges(self, nums, k):
        n = len(nums)
        d = [0] * (2 * k + 2)
        half = n // 2
        for i in range(half):
            x, y = nums[i], nums[-i - 1]
            if x > y:
                x, y = y, x
            d[0] += 1
            d[y - x + 1] -= 1
            d[y + k] += 1
            d[y + k + 1] -= 1
            d[y + k + 1] += 1
        # Accumulate the prefix sums on d
        for i in range(1, len(d)):
            d[i] += d[i - 1]
        return min(d[:2 * k + 1])