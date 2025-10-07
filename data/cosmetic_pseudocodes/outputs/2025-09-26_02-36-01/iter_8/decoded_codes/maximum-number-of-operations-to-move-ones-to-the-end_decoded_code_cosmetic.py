class Solution:
    def maxOperations(self, s: str) -> int:
        result = 0
        tally = 0
        iterator = 0

        while iterator < len(s):
            currentChar = s[iterator]
            if currentChar == '1':
                tally += 1
            else:
                if iterator != 0 and s[iterator - 1] == '1':
                    result += tally
            iterator += 1

        return result