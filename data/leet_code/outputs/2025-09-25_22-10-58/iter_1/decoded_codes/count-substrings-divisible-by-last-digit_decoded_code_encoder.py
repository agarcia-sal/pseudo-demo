class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        total_substrings = 0
        for i in range(n):
            current_number = 0
            for j in range(i, n):
                current_number = current_number * 10 + int(s[j])
                last_digit = int(s[j])
                if last_digit != 0 and current_number % last_digit == 0:
                    total_substrings += 1
        return total_substrings