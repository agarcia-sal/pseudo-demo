class Solution:
    def maxOperations(self, s: str) -> int:
        total = 0
        countOnes = 0
        position = 0
        length = len(s)
        while position < length:
            currentChar = s[position]
            if currentChar == '1':
                countOnes += 1
            elif position > 0:
                prevChar = s[position - 1]
                if prevChar == '1':
                    total += countOnes
            position += 1
        return total