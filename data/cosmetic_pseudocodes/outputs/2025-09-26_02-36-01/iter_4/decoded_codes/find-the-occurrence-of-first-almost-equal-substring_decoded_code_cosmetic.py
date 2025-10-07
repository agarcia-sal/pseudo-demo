class Solution:
    def minStartingIndex(self, s: str, pattern: str) -> int:
        def is_almost_equal(substring: str, pattern: str) -> bool:
            mismatch_counter = 0
            for c_sub, c_pat in zip(substring, pattern):
                if c_sub != c_pat:
                    mismatch_counter += 1
                    if mismatch_counter > 1:
                        return False
            return True

        plength = len(pattern)
        for start_idx in range(len(s) - plength + 1):
            candidate_slice = s[start_idx:start_idx + plength]
            if is_almost_equal(candidate_slice, pattern):
                return start_idx
        return -1