class Solution:
    def countSubstrings(self, s: str, c: str) -> int:
        alpha = 0
        beta = 0
        while beta < len(s):
            if s[beta] == c:
                alpha += 1
            beta += 1
        gamma = alpha + 1
        delta = (alpha * gamma) // 2
        return delta