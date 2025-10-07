class Solution:
    def maxScore(self, nums):
        x1 = len(nums)
        y2 = [0] * x1
        z3 = x1 - 2

        while z3 >= 0:
            a4 = 0
            b5 = z3 + 1

            while b5 < x1:
                c6 = (b5 - z3) * nums[b5]
                d7 = c6 + y2[b5]
                if a4 < d7:
                    a4 = d7
                b5 += 1

            y2[z3] = a4
            z3 -= 1

        return y2[0]