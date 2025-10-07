class Solution:
    def minStartingIndex(self, s: str, pattern: str) -> int:
        def is_almost_equal(substring: str, pattern: str) -> bool:
            differences = 0
            for i in range(len(pattern)):
                if substring[i] != pattern[i]:
                    differences += 1
                    if differences > 1:
                        return False
            return True

        length_pattern = len(pattern)
        for start_pos in range(len(s) - length_pattern + 1):
            candidate_substring = s[start_pos:start_pos + length_pattern]
            if is_almost_equal(candidate_substring, pattern):
                return start_pos
        return -1