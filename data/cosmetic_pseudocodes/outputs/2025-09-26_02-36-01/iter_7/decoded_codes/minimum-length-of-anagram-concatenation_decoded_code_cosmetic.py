class Solution:
    def minAnagramLength(self, s: str) -> int:
        distinctCharacters = set()
        indexCounter = 0
        while indexCounter < len(s):
            currentChar = s[indexCounter]
            distinctCharacters.add(currentChar)
            indexCounter += 1
        result = 0
        for _ in distinctCharacters:
            result += 1
        return result