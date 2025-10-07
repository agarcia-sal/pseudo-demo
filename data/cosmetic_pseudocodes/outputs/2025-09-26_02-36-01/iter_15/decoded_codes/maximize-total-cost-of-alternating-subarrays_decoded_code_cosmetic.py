class Solution:
    def maximumTotalCost(self, nums):
        u7k = len(nums)
        if u7k == 1:
            return nums[0]

        yv4 = [0] * u7k
        yv4[u7k - 1] = nums[u7k - 1]

        w2q = u7k - 2
        while w2q >= 0:
            m5r = nums[w2q]
            if m5r > yv4[w2q + 1]:
                yv4[w2q] = m5r
            else:
                yv4[w2q] = yv4[w2q + 1] + m5r

            ph1 = w2q + 1
            while ph1 <= u7k - 1:
                gp9 = (-1) ** (ph1 - w2q)
                m5r += nums[ph1] * gp9

                if ph1 + 1 < u7k:
                    potential = m5r + yv4[ph1 + 1]
                    if yv4[w2q] < potential:
                        yv4[w2q] = potential
                else:
                    if yv4[w2q] < m5r:
                        yv4[w2q] = m5r

                ph1 += 1
            w2q -= 1

        return yv4[0]