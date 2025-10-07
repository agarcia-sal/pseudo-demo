class Solution:
    def maximumValueSum(self, nums, k, edges):
        acc = 0
        cnt = 0
        least = float('inf')

        for val in nums:
            xres = val ^ k
            diff = xres - val
            if diff > 0:
                cnt += 1

            if val > xres:
                acc += val
            else:
                acc += xres

            abs_diff = diff if diff >= 0 else -diff
            if abs_diff < least:
                least = abs_diff

        if cnt % 2 != 0:
            acc -= least

        return acc