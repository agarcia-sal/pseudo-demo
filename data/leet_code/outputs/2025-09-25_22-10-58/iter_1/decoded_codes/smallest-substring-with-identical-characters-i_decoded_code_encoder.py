class Solution:
    def minLength(self, s: str, numOps: int) -> int:
        def longest_uniform_substring(s):
            max_len = 0
            current_len = 1
            for i in range(1, len(s)):
                if s[i] == s[i - 1]:
                    current_len += 1
                else:
                    if max_len < current_len:
                        max_len = current_len
                    current_len = 1
            return max_len if max_len > current_len else current_len

        min_length = len(s)
        limit = 1 << len(s)
        for i in range(limit):
            if bin(i).count('1') > numOps:
                continue
            new_s = list(s)
            for j in range(len(s)):
                if i & (1 << j):
                    new_s[j] = '1' if new_s[j] == '0' else '0'
            candidate_length = longest_uniform_substring(new_s)
            if min_length > candidate_length:
                min_length = candidate_length

        return min_length