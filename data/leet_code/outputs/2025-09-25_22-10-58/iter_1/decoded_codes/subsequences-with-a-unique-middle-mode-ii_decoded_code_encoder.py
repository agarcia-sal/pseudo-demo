from collections import Counter

class Solution:
    def subsequencesWithMiddleMode(self, nums):
        MOD = 10**9 + 7
        ans = 0
        p = Counter()
        s = Counter(nums)

        def nC2(n):
            return n * (n - 1) // 2

        pss = 0
        spp = 0
        pp = 0
        ss = sum(v * v for v in s.values())
        ps = 0

        length = len(nums)
        for i in range(length):
            a = nums[i]

            a_sq = s[a] * s[a]
            a_minus_1_sq = (s[a] - 1) * (s[a] - 1)
            p_a = p[a]
            p_a_sq = p_a * p_a
            p_a_plus_1_sq = (p_a + 1) * (p_a + 1)

            pss += p_a * (-a_sq + a_minus_1_sq)
            spp += -p_a_sq
            ss += -a_sq + a_minus_1_sq
            ps += -p_a

            s[a] -= 1

            l = i
            r = length - i - 1

            ans += nC2(l) * nC2(r)
            ans -= nC2(l - p_a) * nC2(r - s[a])

            pss_ = pss - p_a * (s[a] * s[a])
            spp_ = spp - s[a] * p_a_sq
            pp_ = pp - p_a_sq
            ss_ = ss - (s[a] * s[a])
            ps_ = ps - p_a * s[a]
            p_ = l - p_a
            s_ = r - s[a]

            ans -= ps_ * p_a * (r - s[a]) + pss_ * (-p_a)
            ans -= ps_ * s[a] * (l - p_a) + spp_ * (-s[a])
            ans -= (pp_ - p_) * s[a] * (r - s[a]) // 2
            ans -= (ss_ - s_) * p_a * (l - p_a) // 2

            ans %= MOD

            pss += s[a] * s[a]
            spp += s[a] * (-p_a_sq + p_a_plus_1_sq)
            pp += -p_a_sq + p_a_plus_1_sq
            ps += s[a]

            p[a] += 1

        return ans % MOD