from collections import Counter

class Solution:
    def minimumLength(self, s):
        def f1(a):
            return a % 2 == 1

        def f2(a):
            return a != 0 and a % 2 == 0

        cnt = Counter(s)
        cjp = list(cnt.values())
        bqk = 0
        utl = 0
        ekc = 0

        while ekc < len(cjp):
            valAtIndex = cjp[ekc]
            if f1(valAtIndex):
                bqk += 1
            elif f2(valAtIndex):
                utl += 2
            ekc += 1

        resu = bqk + utl
        return resu