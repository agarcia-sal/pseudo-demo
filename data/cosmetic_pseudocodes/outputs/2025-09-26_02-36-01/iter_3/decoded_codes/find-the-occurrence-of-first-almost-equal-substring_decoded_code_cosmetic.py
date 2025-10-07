class Solution:
    def minStartingIndex(self, s, pattern):
        def is_almost_equal(substring, pattern):
            mismatch_count = 0
            for char_sub, char_pat in zip(substring, pattern):
                if char_sub != char_pat:
                    mismatch_count += 1
                    if mismatch_count > 1:
                        return False
            return True

        length_pat = len(pattern)
        max_start = len(s) - length_pat
        for start_pos in range(max_start + 1):
            segment = s[start_pos:start_pos + length_pat]
            if is_almost_equal(segment, pattern):
                return start_pos
        return -1