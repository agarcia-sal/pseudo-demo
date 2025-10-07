class Solution:
    def countSubstrings(self, s: str, c: str) -> int:
        frequency = s.count(c)
        total = frequency * (frequency + 1) // 2
        return total