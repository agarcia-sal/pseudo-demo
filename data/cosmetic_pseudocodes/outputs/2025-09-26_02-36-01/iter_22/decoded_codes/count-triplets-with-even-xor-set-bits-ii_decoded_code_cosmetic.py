from typing import List, Tuple

class Solution:
    def tripletCount(self, a: List[int], b: List[int], c: List[int]) -> int:

        def count_even_odd_bits(arr: List[int]) -> Tuple[int, int]:
            k0 = 0
            for val in arr:
                cnt_bits = 0
                x = val
                while x > 0:
                    cnt_bits += x & 1
                    x >>= 1
                if cnt_bits % 2 == 0:
                    k0 += 1
            k1 = len(arr) - k0
            return k0, k1

        p0, p1 = count_even_odd_bits(a)
        q0, q1 = count_even_odd_bits(b)
        r0, r1 = count_even_odd_bits(c)

        m0 = p0 * q0 * r0
        m1 = (p0 * q1 * r1) + (p1 * q0 * r1) + (p1 * q1 * r0)

        ans = m0 + m1
        return ans