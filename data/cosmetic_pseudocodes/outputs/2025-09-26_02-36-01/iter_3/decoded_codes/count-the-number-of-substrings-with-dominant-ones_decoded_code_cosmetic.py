class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        total_substrings = 0
        n = len(s)
        for start in range(n):
            count_one = 0
            count_zero = 0
            for end in range(start, n):
                if s[end] == '1':
                    count_one += 1
                else:
                    count_zero += 1
                if count_one >= count_zero * count_zero:
                    total_substrings += 1
        return total_substrings