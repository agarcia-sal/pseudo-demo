class Solution:
    def maxTotalReward(self, rewardValues):
        m = list(set(rewardValues))  # remove duplicates
        m.sort()

        p = 1
        q = 0
        while q < len(m):
            r = 1 << m[q]
            s = p & (r - 1)
            shift = t_bitlen = r.bit_length() - 1
            t = r
            p = p | (s << shift)
            q += 1

        u = p.bit_length() - 1
        return u