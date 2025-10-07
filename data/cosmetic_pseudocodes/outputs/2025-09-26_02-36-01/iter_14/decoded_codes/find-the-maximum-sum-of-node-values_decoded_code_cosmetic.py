class Solution:
    def maximumValueSum(self, nums, k):
        acc = 0
        cnt = 0
        mn = float('inf')

        for val in nums:
            x = val ^ k
            diff = x - val
            if diff > 0:
                cnt += 1
            acc += x if x > val else val
            if abs(diff) < mn:
                mn = abs(diff)

        if cnt % 2 != 0:
            acc -= mn

        return acc