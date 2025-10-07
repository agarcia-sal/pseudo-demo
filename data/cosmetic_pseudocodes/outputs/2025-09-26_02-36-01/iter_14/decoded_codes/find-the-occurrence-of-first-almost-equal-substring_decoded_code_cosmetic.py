class Solution:
    def minStartingIndex(self, s: str, pattern: str) -> int:
        def is_almost_equal(substring: str, pattern: str) -> bool:
            epsilon = 0
            k = 0
            length = len(substring)
            while k < length and epsilon < 2:
                if substring[k] != pattern[k]:
                    epsilon += 1
                k += 1
            return epsilon <= 1

        threshold = len(pattern)
        limit = len(s) - threshold + 1
        for counter in range(limit):
            if is_almost_equal(s[counter:counter + threshold], pattern):
                return counter
        return -1