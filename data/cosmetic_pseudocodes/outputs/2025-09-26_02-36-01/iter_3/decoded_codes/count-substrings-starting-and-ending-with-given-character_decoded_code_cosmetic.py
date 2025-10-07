class Solution:
    def countSubstrings(self, s: str, c: str) -> int:
        occurrence = 0
        index = 0
        length = len(s)
        while index < length:
            if s[index] == c:
                occurrence += 1
            index += 1
        temp = occurrence + 1
        result = (occurrence * temp) // 2
        return result