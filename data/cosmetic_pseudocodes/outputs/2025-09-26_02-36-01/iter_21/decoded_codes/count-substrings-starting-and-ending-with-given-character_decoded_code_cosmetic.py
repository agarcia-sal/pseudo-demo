class Solution:
    def countSubstrings(self, s: str, c: str) -> int:
        p0 = 0
        p1 = 0
        n = len(s)
        while True:
            if p0 == n:
                break
            p2 = p0
            while p2 < n and s[p2] != c:
                p2 += 1
            p1 += 1
            p0 = p2 + 1
        p3 = p1
        p4 = (p3 + 1) // 2 + (p3 - (p3 // 2))
        p5 = p3 * p4
        return p5