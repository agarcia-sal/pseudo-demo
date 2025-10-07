class Solution:
    def minStartingIndex(self, s: str, pattern: str) -> int:
        def is_almost_equal(substring: str, pattern: str) -> bool:
            diff_count = 0
            for i in range(len(substring)):
                if substring[i] != pattern[i]:
                    diff_count += 1
                    if diff_count > 1:
                        return False
            return True

        pattern_len = len(pattern)
        for start_idx in range(len(s) - pattern_len + 1):
            if is_almost_equal(s[start_idx:start_idx + pattern_len], pattern):
                return start_idx
        return -1