class Solution:
    def minStartingIndex(self, s: str, pattern: str) -> int:
        def is_almost_equal(substring: str) -> bool:
            diff_accumulator = 0
            pos = 0

            while pos < len(substring) and pos < len(pattern):
                if substring[pos] != pattern[pos]:
                    diff_accumulator += 1
                    if diff_accumulator > 1:
                        return False
                pos += 1
            return True

        plen = len(pattern)
        l_s = len(s)
        result = -1

        start_idx = 0
        while start_idx < l_s - plen + 1:
            current_sub = s[start_idx:start_idx + plen]
            if is_almost_equal(current_sub):
                result = start_idx
                break
            start_idx += 1

        return result