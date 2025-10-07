class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        n = len(s)
        count = 0
        for start in range(n):
            ones = 0
            zeros = 0
            for end in range(start, n):
                if s[end] == '1':
                    ones += 1
                else:
                    zeros += 1
                if ones >= zeros * zeros:
                    count += 1
        return count