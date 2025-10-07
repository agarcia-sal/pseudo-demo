from typing import List, Tuple

class Solution:
    def tripletCount(self, a: List[int], b: List[int], c: List[int]) -> int:

        def count_even_odd_bits(arr: List[int]) -> Tuple[int, int]:
            even_count = 0
            for val in reversed(arr):
                bit_sum = 0
                x = val
                while x > 0:
                    bit_sum += x & 1
                    x >>= 1
                if bit_sum % 2 == 0:
                    even_count += 1
            odd_count = len(arr) - even_count
            return even_count, odd_count

        a_even, a_odd = count_even_odd_bits(a)
        b_even, b_odd = count_even_odd_bits(b)
        c_even, c_odd = count_even_odd_bits(c)

        term1 = a_even * b_even * c_even
        term2 = (a_even * b_odd * c_odd) + (a_odd * b_even * c_odd) + (a_odd * b_odd * c_even)

        return term1 + term2