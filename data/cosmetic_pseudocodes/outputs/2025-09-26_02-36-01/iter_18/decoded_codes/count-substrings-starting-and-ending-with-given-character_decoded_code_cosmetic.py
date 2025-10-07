class Solution:
    def countSubstrings(self, s: str, c: str) -> int:
        idx = 0
        totalChars = 0
        accumulator = 0

        while idx < len(s):
            if not (s[idx] != c):
                totalChars += 1
            idx += 1

        tempSum = 0
        iter = 1

        while iter <= totalChars:
            tempSum += iter
            iter += 1

        accumulator = totalChars * tempSum

        output = accumulator
        return output