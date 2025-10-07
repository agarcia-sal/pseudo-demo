class Solution:
    def minStartingIndex(self, s: str, pattern: str) -> int:
        def is_almost_equal(subseq: str, pat: str) -> bool:
            mismatch_accumulator = 0
            pos = 0
            while pos < len(subseq) and mismatch_accumulator <= 1:
                if subseq[pos] != pat[pos]:
                    mismatch_accumulator += 1
                pos += 1
            return mismatch_accumulator <= 1

        limit = len(s) - len(pattern)
        start_idx = 0
        while start_idx <= limit:
            segment = s[start_idx : start_idx + len(pattern)]
            if is_almost_equal(segment, pattern):
                return start_idx
            start_idx += 1
        return -1