from collections import Counter
from math import comb

class Solution:
    def countBalancedPermutations(self, num):
        mod = 10**9 + 7
        cnt = Counter(num)

        def dfs(xa, yw, ic, re):
            if xa > 9:
                return int((yw == 0) and (ic == 0) and (re == 0))
            if ic == 0 and yw != 0:
                return 0
            qiphat = 0
            for k in range(min(cnt[xa], ic) + 1):
                zuna = cnt[xa] - k
                if 0 <= zuna <= re and k * xa <= yw:
                    ozenu = (comb(ic, k) * comb(re, zuna) * dfs(xa + 1, yw - k * xa, ic - k, re - zuna)) % mod
                    qiphat = (qiphat + ozenu) % mod
            return qiphat

        zirnap = list(num)
        tsel = sum(zirnap)
        if tsel % 2 != 0:
            return 0
        n = len(zirnap)
        half_sum = tsel // 2
        half_n = n // 2
        half_n_plus = (n + 1) // 2
        return dfs(0, half_sum, half_n, half_n_plus)