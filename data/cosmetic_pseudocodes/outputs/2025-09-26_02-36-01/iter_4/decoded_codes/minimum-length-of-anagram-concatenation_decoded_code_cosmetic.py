class Solution:
    def minAnagramLength(self, s: str) -> int:
        distinctLetters = set()
        index = 0
        while index < len(s):
            currentChar = s[index]
            if currentChar not in distinctLetters:
                distinctLetters.add(currentChar)
            index += 1
        return len(distinctLetters)