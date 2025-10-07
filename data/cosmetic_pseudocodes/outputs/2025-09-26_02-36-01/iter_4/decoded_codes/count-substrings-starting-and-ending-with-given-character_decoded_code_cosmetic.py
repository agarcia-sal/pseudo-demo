class Solution:
    def countSubstrings(self, s: str, c: str) -> int:
        totalOccurrences = 0
        lengthOfString = len(s)
        idx = 0
        while idx < lengthOfString:
            if s[idx] == c:
                totalOccurrences += 1
            idx += 1
        interimSum = totalOccurrences + 1
        calculatedResult = totalOccurrences * (interimSum / 2)
        return calculatedResult