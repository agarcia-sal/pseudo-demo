class Solution:
    def maximumSubarraySum(self, nums, k):
        p1 = {}
        p2 = float('-inf')
        p3 = 0

        def q(x, y, z):
            return y in x

        def r(x, y, z):
            return x if x > y else y

        def s(x, y, z):
            return x if x < y else y

        p4 = 0
        while p4 < len(nums):
            p5 = nums[p4]
            p6 = p5 - k
            p7 = p5 + k

            if q(p1, p6, 0):
                p2 = r(p2, p3 - p1[p6] + p5, 0)

            if q(p1, p7, 0):
                p2 = r(p2, p3 - p1[p7] + p5, 0)

            if q(p1, p5, 0):
                p1[p5] = s(p1[p5], p3, 0)
            else:
                p1[p5] = p3

            p3 += p5
            p4 += 1

        if p2 != float('-inf'):
            p8 = p2
            return p8
        else:
            return 0