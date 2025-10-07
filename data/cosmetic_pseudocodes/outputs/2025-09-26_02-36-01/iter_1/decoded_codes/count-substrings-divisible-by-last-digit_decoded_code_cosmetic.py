class Solution:
    def countSubstrings(self, s: str) -> int:
        count = 0
        length = len(s)
        for startIndex in range(length):
            num = 0
            for endIndex in range(startIndex, length):
                digit = int(s[endIndex])
                num = num * 10 + digit
                if digit != 0 and num % digit == 0:
                    count += 1
        return count