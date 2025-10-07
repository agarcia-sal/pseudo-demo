class Solution:
    def maxOperations(self, s: str) -> int:
        resultHolder = 0
        accumulator = 0
        position = 0
        while position < len(s):
            if s[position] == '1':
                accumulator += 1
            else:
                if position > 0 and s[position - 1] == '1':
                    resultHolder += accumulator
            position += 1
        return resultHolder