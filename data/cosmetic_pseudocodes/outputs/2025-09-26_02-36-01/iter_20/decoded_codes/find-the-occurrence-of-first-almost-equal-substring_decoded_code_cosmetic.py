class Solution:
    def minStartingIndex(self, s: str, pattern: str) -> int:
        def is_almost_equal(substring: str, pattern: str) -> bool:
            alpha = 0  # count of mismatches
            for beta in range(len(substring)):
                gamma = substring[beta]
                delta = pattern[beta]
                epsilon = 0 if gamma == delta else 1
                alpha += epsilon
                if alpha > 1:
                    return False
            return True

        mu = len(pattern)
        nu = 0
        while nu <= len(s) - mu:
            eta = s[nu : nu + mu]
            if is_almost_equal(eta, pattern):
                return nu
            nu += 1
        return -1