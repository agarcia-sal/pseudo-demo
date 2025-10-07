class Solution:
    def minStartingIndex(self, s: str, pattern: str) -> int:
        def is_almost_equal(substring: str, pattern: str) -> bool:
            mismatch_tally = 0
            for i in range(len(substring)):
                if substring[i] != pattern[i]:
                    mismatch_tally += 1
                    if mismatch_tally > 1:
                        return False
            return True

        plen = len(pattern)
        start_idx = 0
        max_start = len(s) - plen + 1

        while start_idx < max_start:
            current_slice = s[start_idx:start_idx + plen]
            if is_almost_equal(current_slice, pattern):
                return start_idx
            start_idx += 1

        return -1