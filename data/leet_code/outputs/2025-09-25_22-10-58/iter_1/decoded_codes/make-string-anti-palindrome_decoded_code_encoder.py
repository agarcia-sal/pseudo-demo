class Solution:
    def makeAntiPalindrome(self, s: str) -> str:
        cs = sorted(s)
        n = len(cs)
        m = n // 2

        if m > 0 and cs[m] == cs[m - 1]:
            i = m
            while i < n and cs[i] == cs[i - 1]:
                i += 1
            j = m
            while j < n and cs[j] == cs[n - j - 1]:
                if i >= n:
                    return "-1"
                cs[i], cs[j] = cs[j], cs[i]
                i += 1
                j += 1

        for i in range(m):
            if cs[i] == cs[n - i - 1]:
                swapped = False
                for k in range(m, n):
                    if cs[k] != cs[i] and cs[k] != cs[n - i - 1]:
                        cs[k], cs[i] = cs[i], cs[k]
                        swapped = True
                        break
                if not swapped:
                    return "-1"

        return "".join(cs)