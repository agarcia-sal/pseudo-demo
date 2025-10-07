from collections import Counter, defaultdict

class Solution:
    def subsequencesWithMiddleMode(self, nums):
        MOD = 10**9 + 7
        outcome = 0
        prefixCounts = defaultdict(int)
        suffixCounts = Counter(nums)

        def comb2(x):
            if x < 2:
                return 0
            return x * (x - 1) // 2

        val_pss = 0
        val_spp = 0
        val_pp = 0
        acc_ss = 0
        val_ps = 0

        n = len(nums)
        for idx in range(n):
            elem = nums[idx]

            squaresfx = suffixCounts[elem]
            squaresfx_prev = squaresfx - 1

            val_pss += prefixCounts[elem] * (-(squaresfx * squaresfx) + (squaresfx_prev * squaresfx_prev))
            val_spp += (-(prefixCounts[elem] * prefixCounts[elem]))
            acc_ss += (-(squaresfx * squaresfx)) + (squaresfx_prev * squaresfx_prev)
            val_ps += (-(prefixCounts[elem]))

            suffixCounts[elem] -= 1

            left_length = idx
            right_length = n - idx - 1

            outcome += comb2(left_length) * comb2(right_length)

            pl = prefixCounts[elem]
            sr = suffixCounts[elem]

            outcome -= comb2(left_length - pl) * comb2(right_length - sr)

            val_pss_adj = val_pss - pl * (sr * sr)
            val_spp_adj = val_spp - sr * (pl * pl)
            val_pp_adj = val_pp - (pl * pl)
            acc_ss_adj = acc_ss - (sr * sr)
            val_ps_adj = val_ps - pl * sr
            prefix_adj = left_length - pl
            suffix_adj = right_length - sr

            outcome -= val_ps_adj * pl * suffix_adj + val_pss_adj * (-pl)
            outcome -= val_ps_adj * sr * prefix_adj + val_spp_adj * (-sr)
            outcome -= (val_pp_adj - prefix_adj) * sr * suffix_adj / 2
            outcome -= (acc_ss_adj - suffix_adj) * pl * prefix_adj / 2

            outcome %= MOD

            val_pss += sr * sr
            val_spp += sr * (-(pl * pl)) + (pl + 1) * (pl + 1)
            val_pp += (-(pl * pl)) + (pl + 1) * (pl + 1)
            val_ps += sr

            prefixCounts[elem] += 1

        return outcome % MOD