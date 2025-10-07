class Solution:
    def minStartingIndex(self, s, pattern):
        def is_almost_equal(substring, pattern):
            delta = 0
            for ch_sub, ch_pat in zip(substring, pattern):
                if ch_sub != ch_pat:
                    delta += 1
                    if delta > 1:
                        return False
            return True

        limit = len(s) - len(pattern)
        idx = 0
        while idx <= limit:
            segment = s[idx:idx + len(pattern)]
            if is_almost_equal(segment, pattern):
                return idx
            idx += 1
        return -1