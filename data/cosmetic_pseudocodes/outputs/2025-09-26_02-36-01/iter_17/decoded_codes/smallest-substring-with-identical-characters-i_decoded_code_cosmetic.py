class Solution:
    def minLength(self, s, numOps):
        def longest_uniform_substring(s):
            a = 0
            b = 1
            c = 1
            while b < len(s):
                if s[b] == s[b - 1]:
                    c += 1
                else:
                    if a < c:
                        a = c
                    c = 1
                b += 1
            return a if a > c else c

        x = len(s)
        y = 1 << x
        z = x
        i = 0
        while i < y:
            if bin(i).count('1') > numOps:
                i += 1
                continue

            arr = list(s)
            j = 0
            while j < x:
                if (i & (1 << j)) != 0:
                    arr[j] = '1' if arr[j] == '0' else '0'
                j += 1

            candidate = longest_uniform_substring(arr)
            if z > candidate:
                z = candidate

            i += 1

        return z