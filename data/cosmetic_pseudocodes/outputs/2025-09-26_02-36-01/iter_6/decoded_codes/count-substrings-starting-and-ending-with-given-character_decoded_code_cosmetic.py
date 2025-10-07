class Solution:
    def countSubstrings(self, c: str, s: str) -> float:
        totalMatches = 0
        lengthValue = 0
        hitCounter = 0
        finalAnswer = 0

        lengthValue = 0
        while lengthValue < len(s):
            if not (s[lengthValue] != c):
                hitCounter += 1
            lengthValue += 1

        totalMatches = hitCounter * ((hitCounter + 1) / ((1 + 1) + 0))
        finalAnswer = totalMatches
        return finalAnswer