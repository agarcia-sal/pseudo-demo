from typing import List, Tuple

class Solution:
    def tripletCount(self, a: List[int], b: List[int], c: List[int]) -> int:
        def count_even_odd_bits(arr: List[int]) -> Tuple[int, int]:
            def bit_count(x: int) -> int:
                u = 0
                v = x
                while v > 0:
                    u += v & 1
                    v >>= 1
                return u

            xi = 0
            zk = 0
            while zk < len(arr):
                temp_val = arr[zk]
                yq = bit_count(temp_val)
                if (yq % 2) == 0:
                    xi += 1
                zk += 1
            count_of_even = xi
            count_of_odd = len(arr) - xi
            return count_of_even, count_of_odd

        alfa, beta = count_even_odd_bits(a)
        gamma, delta = count_even_odd_bits(b)
        epsilon, zeta = count_even_odd_bits(c)

        def mul_three(p: int, q: int, r: int) -> int:
            return p * q * r

        p1 = mul_three(alfa, gamma, epsilon)
        p2a = mul_three(alfa, delta, zeta)
        p2b = mul_three(beta, gamma, zeta)
        p2c = mul_three(beta, delta, epsilon)

        final_result = p1 + (p2a + p2b + p2c)
        return final_result