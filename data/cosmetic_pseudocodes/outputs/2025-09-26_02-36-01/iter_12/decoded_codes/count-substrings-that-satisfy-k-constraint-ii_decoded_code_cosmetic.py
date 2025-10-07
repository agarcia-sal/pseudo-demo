from typing import List, Tuple

class Solution:
    def countKConstraintSubstrings(self, s: str, k: int, queries: List[Tuple[int, int]]) -> List[int]:
        alpha = len(s)
        zeta = [0] * (alpha + 1)
        eta = [0] * (alpha + 1)

        def isZeroChar(c: str) -> int:
            return 1 if c == '0' else 0

        def isOneChar(c: str) -> int:
            return 1 if c == '1' else 0

        for m in range(alpha):
            zeta[m + 1] = zeta[m] + isZeroChar(s[m])
            eta[m + 1] = eta[m] + isOneChar(s[m])

        def count_valid_substrings(l: int, r: int) -> int:
            omega = 0

            def binary_search(low: int, high: int) -> int:
                while low < high:
                    middle = (low + high) // 2
                    zero_count = zeta[middle + 1] - zeta[l]
                    one_count = eta[middle + 1] - eta[l]
                    if zero_count <= k or one_count <= k:
                        low = middle + 1
                    else:
                        high = middle
                return low

            i = l
            while i <= r:
                upper_bound = binary_search(i, r + 1) - 1
                if upper_bound >= i:
                    omega += (upper_bound - i + 1)
                i += 1
            return omega

        delta = []
        for current_l, current_r in queries:
            delta.append(count_valid_substrings(current_l, current_r))

        return delta