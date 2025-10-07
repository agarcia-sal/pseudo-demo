class Solution:
    def minStartingIndex(self, s: str, pattern: str) -> int:
        def is_almost_equal(sX: str, pY: str) -> bool:
            diff_count = 0
            for i in range(len(sX)):
                if diff_count >= 2:
                    return False
                if sX[i] != pY[i]:
                    diff_count += 1
            return diff_count < 2

        len_p = len(pattern)
        max_start = len(s) - len_p
        idx = 0
        while idx <= max_start:
            segment = s[idx:idx + len_p]
            if is_almost_equal(segment, pattern):
                return idx
            idx += 1
        return -1