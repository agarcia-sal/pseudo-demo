class Solution:
    def minAnagramLength(self, s: str) -> int:
        auxSet = set()
        idx = 0
        while idx < len(s):
            currentChar = s[idx]
            auxSet.add(currentChar)
            idx += 1
        return len(auxSet)