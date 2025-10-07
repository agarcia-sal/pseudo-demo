class Solution:
    def minStartingIndex(self, s: str, pattern: str) -> int:
        def is_almost_equal(substr: str, pat: str) -> bool:
            mismatch_counter = 0
            for ch_sub, ch_pat in zip(substr, pat):
                if ch_sub != ch_pat:
                    mismatch_counter += 1
                    if mismatch_counter > 1:
                        return False
            return True

        pat_len = len(pattern)
        current_idx = 0
        while current_idx + pat_len <= len(s):
            segment = s[current_idx:current_idx + pat_len]
            if is_almost_equal(segment, pattern):
                return current_idx
            current_idx += 1

        return -1