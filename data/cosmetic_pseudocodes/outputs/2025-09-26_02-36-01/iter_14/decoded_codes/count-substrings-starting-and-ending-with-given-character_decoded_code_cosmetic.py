class Solution:
    def countSubstrings(self, s: str, c: str) -> int:
        alpha = 0
        beta = 0
        gamma = len(s)
        while beta != gamma:
            if s[beta] == c:
                alpha += 1
            beta += 1
        delta = alpha * ((alpha + 1) // 2)
        return delta