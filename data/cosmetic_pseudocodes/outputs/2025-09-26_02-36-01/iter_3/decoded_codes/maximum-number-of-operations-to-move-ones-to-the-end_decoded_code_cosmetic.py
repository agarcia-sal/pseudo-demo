class Solution:
    def maxOperations(self, s: str) -> int:
        result = 0
        tally = 0
        position = 0
        while position < len(s):
            currentChar = s[position]
            if currentChar == '1':
                tally += 1
            else:
                if position > 0:
                    previousChar = s[position - 1]
                    if previousChar == '1':
                        result += tally
            position += 1
        return result