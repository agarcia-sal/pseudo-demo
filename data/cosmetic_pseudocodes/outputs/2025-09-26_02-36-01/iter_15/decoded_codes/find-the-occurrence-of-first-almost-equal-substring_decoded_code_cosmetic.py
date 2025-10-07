class Solution:
    def minStartingIndex(self, s: str, pattern: str) -> int:
        def is_almost_equal(substring, pattern):
            delta = 0
            u = 0
            while u < len(substring) and u < len(pattern):
                if substring[u] != pattern[u]:
                    delta += 1
                    if delta > 1:
                        return False
                u += 1
            return True

        max_i = len(s) - len(pattern)
        k = 0
        while k <= max_i:
            sub = s[k:k+len(pattern)]
            if is_almost_equal(sub, pattern):
                return k
            k += 1
        return -1