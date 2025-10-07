class Solution:
    def minStartingIndex(self, s: str, pattern: str) -> int:
        def is_almost_equal(substring: str) -> bool:
            delta_counter = 0
            for c1, c2 in zip(substring, pattern):
                if c1 != c2:
                    delta_counter += 1
                    if delta_counter > 1:
                        return False
            return True

        pl = len(pattern)
        s_len = len(s)
        j = 0
        while j <= s_len - pl:
            if is_almost_equal(s[j : j + pl]):
                return j
            j += 1
        return -1