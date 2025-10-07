class Solution:
    def maxOperations(self, s: str) -> int:
        result = 0
        tally = 0
        pos = 0
        while pos < len(s):
            currentChar = s[pos]
            if currentChar == "1":
                tally += 1
            else:
                if pos > 0:
                    prevChar = s[pos - 1]
                    if prevChar == "1":
                        result += tally
            pos += 1
        return result