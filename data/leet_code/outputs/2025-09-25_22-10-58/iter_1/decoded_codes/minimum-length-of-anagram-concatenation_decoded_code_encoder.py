class Solution:
    def minAnagramLength(self, s: str) -> int:
        unique_chars = set(s)
        return len(unique_chars)