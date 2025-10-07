from typing import List, Tuple

class Solution:
    def tripletCount(self, a: List[int], b: List[int], c: List[int]) -> int:
        def count_even_odd_bits(arr: List[int]) -> Tuple[int, int]:
            p1 = 0  # count of numbers with even number of set bits
            for val in arr:
                bit_sum = 0
                temp = val
                while temp > 0:
                    bit_sum += temp & 1
                    temp >>= 1
                if bit_sum % 2 == 0:
                    p1 += 1
            p2 = len(arr) - p1  # count of numbers with odd number of set bits
            return p1, p2

        x1, y1 = count_even_odd_bits(a)
        x2, y2 = count_even_odd_bits(b)
        x3, y3 = count_even_odd_bits(c)

        s1 = (x1 * x2) * x3
        s2 = ((x1 * y2) * y3) + ((y1 * x2) * y3) + ((y1 * y2) * x3)
        total = s1 + s2
        return total