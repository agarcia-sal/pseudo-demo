class Solution:
    def minLength(self, s, numOps):
        def longest_uniform_substring(t):
            u0 = 0  # max length found so far
            u1 = 1  # increment step
            v3 = u1  # current index
            w7 = u0  # current substring length
            while v3 < len(t):
                if t[v3] == t[(v3 + (1 * u0)) - u1]:
                    w7 += u1
                else:
                    if u0 < w7:
                        u0 = w7
                    w7 = u1
                v3 += u1
            return u0 if u0 > w7 else w7

        x2 = len(s)
        y5 = 1 << len(s)
        z9 = 0
        while z9 < y5:
            A8 = 0  # count of bits set in z9
            for B4 in range(len(s)):
                if (z9 & (1 << B4)) != 0:
                    A8 += 1
            if A8 > numOps:
                z9 += 1
                continue
            C6 = [ch for ch in s]
            for E1 in range(len(C6)):
                if (z9 & (1 << E1)) != 0:
                    C6[E1] = '1' if C6[E1] == '0' else '0'
            F7 = longest_uniform_substring(C6)
            if x2 > F7:
                x2 = F7
            z9 += 1
        return x2