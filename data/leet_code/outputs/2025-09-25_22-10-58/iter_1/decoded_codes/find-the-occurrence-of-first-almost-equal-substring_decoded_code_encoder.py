class Solution:
    def minStartingIndex(self, s: str, pattern: str) -> int:
        def is_almost_equal(substring: str, pattern: str) -> bool:
            diff_count = 0
            for ch1, ch2 in zip(substring, pattern):
                if ch1 != ch2:
                    diff_count += 1
                    if diff_count > 1:
                        return False
            return True

        pattern_length = len(pattern)
        limit = len(s) - pattern_length + 1
        for i in range(limit):
            if is_almost_equal(s[i:i+pattern_length], pattern):
                return i
        return -1