class Solution:
    def countSubstrings(self, s: str, c: str) -> int:
        occurrence = 0
        for ch in s:
            if ch == c:
                occurrence += 1
        tally = occurrence * ((occurrence + 1) // 2)
        return tally