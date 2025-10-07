class Solution:
    def countSubstrings(self, s: str, c: str) -> int:
        n = len(s)
        char_count = s.count(c)
        result = char_count * (char_count + 1) // 2
        return result