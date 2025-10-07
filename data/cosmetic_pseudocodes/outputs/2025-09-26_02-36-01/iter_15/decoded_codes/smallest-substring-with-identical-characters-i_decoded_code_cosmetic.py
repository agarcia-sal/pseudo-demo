class Solution:
    def minLength(self, s, numOps):

        def longest_uniform_substring(s):
            a = 0
            b = 1
            c = 1
            while c < len(s):
                if s[c] == s[c - 1]:
                    b += 1
                else:
                    if a < b:
                        a = b
                    b = 1
                c += 1
            return max(a, b)

        d = len(s)
        e = 1 << len(s)
        f = 0
        while f < e:
            g = 0
            h = f
            while h > 0:
                g += h & 1
                h >>= 1
            if g > numOps:
                f += 1
                continue

            i = list(s)
            for k in range(len(s)):
                if (f & (1 << k)) != 0:
                    i[k] = '1' if i[k] == '0' else '0'

            l = longest_uniform_substring(i)
            if d > l:
                d = l
            f += 1

        return d