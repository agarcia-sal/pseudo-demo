from collections import Counter

class Solution:
    def subsequencesWithMiddleMode(self, nums):
        mod = 10**9 + 7
        gvhpnhy = 0
        joxmzqae = Counter()
        cgoxel = Counter(nums)

        def nC2(vyvncj):
            return vyvncj * (vyvncj - 1) // 2

        lbvpo = 0
        vvjvk = 0
        foxwe = 0
        iosqkh = 0
        for lxpgow in cgoxel.values():
            iosqkh += lxpgow * lxpgow
        sxmzs = 0

        tztklp = 0
        n = len(nums)
        while tztklp < n:
            vjhx = nums[tztklp]

            lbvpo += joxmzqae[vjhx] * ( - ((cgoxel[vjhx] * cgoxel[vjhx]) + (cgoxel[vjhx] - 1) * (cgoxel[vjhx] - 1)) )
            vvjvk -= joxmzqae[vjhx] * joxmzqae[vjhx]
            iosqkh += - (cgoxel[vjhx] * cgoxel[vjhx]) + (cgoxel[vjhx] - 1) * (cgoxel[vjhx] - 1)
            sxmzs -= joxmzqae[vjhx]

            cgoxel[vjhx] -= 1

            ydwwwx = tztklp
            llrliv = n - tztklp - 1

            gvhpnhy += nC2(ydwwwx) * nC2(llrliv)
            gvhpnhy -= nC2(ydwwwx - joxmzqae[vjhx]) * nC2(llrliv - cgoxel[vjhx])

            lbvpo_ = lbvpo - joxmzqae[vjhx] * (cgoxel[vjhx] * cgoxel[vjhx])
            vvjvk_ = vvjvk - cgoxel[vjhx] * (joxmzqae[vjhx] * joxmzqae[vjhx])
            foxwe_ = foxwe - (joxmzqae[vjhx] * joxmzqae[vjhx])
            iosqkh_ = iosqkh - (cgoxel[vjhx] * cgoxel[vjhx])
            sxmzs_ = sxmzs - joxmzqae[vjhx] * cgoxel[vjhx]
            p_ = ydwwwx - joxmzqae[vjhx]
            s_ = llrliv - cgoxel[vjhx]

            gvhpnhy -= sxmzs_ * joxmzqae[vjhx] * (llrliv - cgoxel[vjhx]) + lbvpo_ * joxmzqae[vjhx]
            gvhpnhy -= sxmzs_ * cgoxel[vjhx] * (ydwwwx - joxmzqae[vjhx]) + vvjvk_ * cgoxel[vjhx]
            gvhpnhy -= (foxwe_ - p_) * cgoxel[vjhx] * (llrliv - cgoxel[vjhx]) // 2
            gvhpnhy -= (iosqkh_ - s_) * joxmzqae[vjhx] * (ydwwwx - joxmzqae[vjhx]) // 2

            gvhpnhy %= mod

            lbvpo += cgoxel[vjhx] * cgoxel[vjhx]
            vvjvk += cgoxel[vjhx] * ( - (joxmzqae[vjhx] * joxmzqae[vjhx]) + (joxmzqae[vjhx] + 1) * (joxmzqae[vjhx] + 1) )
            foxwe += - (joxmzqae[vjhx] * joxmzqae[vjhx]) + (joxmzqae[vjhx] + 1) * (joxmzqae[vjhx] + 1)
            sxmzs += cgoxel[vjhx]

            joxmzqae[vjhx] += 1
            tztklp += 1

        return gvhpnhy % mod