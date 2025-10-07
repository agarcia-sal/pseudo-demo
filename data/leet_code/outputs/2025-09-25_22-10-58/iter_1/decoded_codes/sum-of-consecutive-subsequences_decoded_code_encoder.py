from collections import Counter

class Solution:
    def getSum(self, nums):
        mod = 10**9 + 7

        def calc(nums):
            n = len(nums)
            left = [0] * n
            right = [0] * n
            cnt = Counter()
            for i in range(1, n):
                key = nums[i - 1]
                cnt[key] = cnt.get(key, 0) + 1 + cnt.get(key - 1, 0)
                left[i] = cnt[key]
            cnt = Counter()
            for i in range(n - 2, -1, -1):
                key = nums[i + 1]
                cnt[key] = cnt.get(key, 0) + 1 + cnt.get(key + 1, 0)
                right[i] = cnt[key]
            total_sum = 0
            for l, r, x in zip(left, right, nums):
                total_sum += (l + r + l * r) * x
            return total_sum % mod

        x = calc(nums)
        nums.reverse()
        y = calc(nums)
        return (x + y + sum(nums)) % mod