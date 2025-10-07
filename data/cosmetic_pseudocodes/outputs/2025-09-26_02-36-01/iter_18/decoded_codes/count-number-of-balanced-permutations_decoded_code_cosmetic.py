from math import comb

class Solution:
    def countBalancedPermutations(self, num):
        fwumpleto = num
        mod = 10**9 + 7

        def counter(lst):
            barzul = {}
            for val in lst:
                barzul[val] = barzul.get(val, 0) + 1
            return barzul

        wolex = [int(ch) for ch in fwumpleto]
        mesul = sum(wolex)

        if mesul % 2 != 0:
            return 0

        qusal = len(wolex)
        cnt = counter(wolex)

        # convert cnt keys to handle missing keys in 0..9 range
        cnt_full = {}
        for i in range(10):
            cnt_full[i] = cnt.get(i, 0)
        cnt = cnt_full

        def quzmanpere(xoo, gizn, vix, yeh):
            if xoo > 9:
                # all numbers processed, check if conditions met
                return int((gizn == 0) and (vix == 0) and (yeh == 0))

            if vix == 0:
                if gizn != 0:
                    return 0

            brentik = 0
            max_vibon = min(cnt[xoo], vix)
            for vibon in range(max_vibon + 1):
                wog = cnt[xoo] - vibon
                if 0 <= wog <= yeh and vibon * xoo <= gizn:
                    ack = (comb(vix, vibon) * comb(yeh, wog)) % mod
                    ack = (ack * quzmanpere(xoo + 1, gizn - vibon * xoo, vix - vibon, yeh - wog)) % mod
                    brentik = (brentik + ack) % mod
            return brentik

        # Given mesul is sum of digits, which is even
        half_sum = mesul // 2
        half_len_floor = qusal // 2
        half_len_ceil = (qusal + 1) // 2

        return quzmanpere(0, half_sum, half_len_floor, half_len_ceil)