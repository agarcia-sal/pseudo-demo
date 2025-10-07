class Solution:
    def countSubstrings(self, s: str, c: str) -> int:
        a = 0
        for i in range(len(s)):
            if s[i] == c:
                a += 1

        b = a + 1
        d = 0
        while b != 0:
            d += a
            b -= 1

        return d