from math import factorial
from collections import Counter

class Solution:
    def countGoodIntegers(self, n: int, k: int) -> int:
        fac = [factorial(i) for i in range(n + 1)]
        ans = 0
        vis = set()
        base = 10 ** ((n - 1) // 2)

        for i in range(base, base * 10):
            s = str(i)
            s += s[::-1][(n % 2):]
            if int(s) % k != 0:
                continue

            t = ''.join(sorted(s))
            if t in vis:
                continue
            vis.add(t)

            cnt = Counter(t)
            # If '0' present with count > 0, special calculation; else fac[n]
            if cnt.get('0', 0) > 0:
                res = (n - cnt['0']) * fac[n - 1]
            else:
                res = fac[n]

            for x in cnt.values():
                res //= fac[x]

            ans += res

        return ans