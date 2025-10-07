class Solution:
    def countSubstrings(self, s: str, c: str) -> int:
        t3 = 0
        for ch in s:
            if ch == c:
                t3 += 1
        t4 = t3 * (t3 + 1) // 2
        return t4