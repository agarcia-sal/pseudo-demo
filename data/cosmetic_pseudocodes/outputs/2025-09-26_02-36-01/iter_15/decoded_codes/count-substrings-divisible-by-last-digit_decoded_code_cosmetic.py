class Solution:
    def countSubstrings(self, s: str) -> int:
        length = len(s)
        count = 0
        start = 0
        while start < length:
            end = start
            num = 0
            while True:
                digit = int(s[end])
                num = num * 10 + digit
                # Check if digit is non-zero and num mod digit is zero
                if digit != 0 and num % digit == 0:
                    count += 1
                end += 1
                if end >= length:
                    break
            start += 1
        return count