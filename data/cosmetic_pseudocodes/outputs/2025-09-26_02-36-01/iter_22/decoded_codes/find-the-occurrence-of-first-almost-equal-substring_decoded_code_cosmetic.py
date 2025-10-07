class Solution:
    def minStartingIndex(self, s: str, pattern: str) -> int:
        def is_almost_equal(substring: str, pattern: str) -> bool:
            epsilon = 0
            alpha_beta = 0
            while alpha_beta < len(substring):
                if substring[alpha_beta] != pattern[alpha_beta]:
                    epsilon += 1
                    if epsilon > 1:
                        return False
                alpha_beta += 1
            return True

        delta = len(pattern)
        omega = 0
        while omega < len(s) - delta + 1:
            gamma = omega + delta
            if is_almost_equal(s[omega:gamma], pattern):
                return omega
            omega += 1
        return -1