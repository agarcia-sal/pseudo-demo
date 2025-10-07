class Solution:
    def countSubstrings(self, s: str, c: str) -> int:
        lengthOfString = 0
        index = 0

        while index < len(s):
            lengthOfString += 1
            index += 1

        index = 0
        totalOccurrences = 0

        while index < lengthOfString:
            if s[index] == c:
                totalOccurrences += 1
            index += 1

        interimResult = totalOccurrences * ((totalOccurrences + 1) // 2)

        return interimResult