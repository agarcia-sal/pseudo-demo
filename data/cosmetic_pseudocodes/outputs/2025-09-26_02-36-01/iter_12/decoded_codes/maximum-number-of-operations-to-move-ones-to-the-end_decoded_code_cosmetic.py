class Solution:
    def maxOperations(self, s: str) -> int:
        def isOne(x: str) -> bool:
            return x == "1"

        result = 0
        tally = 0
        position = 0

        while position < len(s):
            currentChar = s[position]
            if isOne(currentChar):
                tally += 1
            else:
                if position > 0:
                    prevChar = s[position - 1]
                    if isOne(prevChar):
                        result += tally
            position += 1

        return result