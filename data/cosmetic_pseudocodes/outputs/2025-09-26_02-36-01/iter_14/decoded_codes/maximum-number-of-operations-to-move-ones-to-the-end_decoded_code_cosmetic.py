class Solution:
    def maxOperations(self, s: str) -> int:
        result = 0
        accumulator = 0
        iterator = 0
        n = len(s)
        while iterator < n:
            if not (s[iterator] != '1'):
                accumulator += 1
            else:
                if iterator > 0 and s[iterator - 1] == '1':
                    result += accumulator
            iterator += 1
        return result