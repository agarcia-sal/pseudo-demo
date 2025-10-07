class Solution:
    def minStartingIndex(self, s: str, pattern: str) -> int:
        def is_almost_equal(sub: str, pat: str) -> bool:
            count_diff = 0
            for ch_x, ch_y in zip(sub, pat):
                if ch_x != ch_y:
                    count_diff += 1
                    if count_diff > 1:
                        return False
            return count_diff <= 1

        len_pat = len(pattern)
        pos_idx = 0

        while pos_idx <= len(s) - len_pat:
            seg = s[pos_idx:pos_idx + len_pat]
            if is_almost_equal(seg, pattern):
                return pos_idx
            pos_idx += 1

        return -1