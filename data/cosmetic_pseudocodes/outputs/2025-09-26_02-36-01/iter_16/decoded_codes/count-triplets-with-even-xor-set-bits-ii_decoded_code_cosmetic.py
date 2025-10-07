from typing import List, Tuple

class Solution:
    def tripletCount(self, a: List[int], b: List[int], c: List[int]) -> int:
        def count_even_odd_bits(arr: List[int]) -> Tuple[int, int]:
            M = 0  # count of numbers with "even adjusted" bit parity
            for x in arr:
                sum_ones = 0
                val = x
                while val > 0:
                    sum_ones += val & 1
                    val >>= 1
                # check parity condition as in pseudocode:
                # (((sum_ones + 2) % 2) + 0) % 2 == 0 simplifies to sum_ones % 2 == 0
                if (sum_ones % 2) == 0:
                    M += 1
            N = len(arr) - M
            return M, N

        p1, p2 = count_even_odd_bits(a)
        q1, q2 = count_even_odd_bits(b)
        r1, r2 = count_even_odd_bits(c)

        v1 = p1 * q1 * r1
        v2 = (p1 * q2 * r2) + (p2 * q1 * r2) + (p2 * q2 * r1)

        w = v1 + v2
        return w