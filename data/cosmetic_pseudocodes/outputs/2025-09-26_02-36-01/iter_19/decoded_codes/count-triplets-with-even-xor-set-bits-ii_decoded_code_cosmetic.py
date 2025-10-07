from typing import List, Tuple

class Solution:
    def tripletCount(self, a: List[int], b: List[int], c: List[int]) -> int:
        def count_even_odd_bits(arr: List[int]) -> Tuple[int, int]:
            tally_even = 0
            for num in arr:
                bit_sum = 0
                temp = num
                while temp > 0:
                    bit_sum += temp & 1
                    temp >>= 1
                if bit_sum % 2 == 0:
                    tally_even += 1
            tally_odd = len(arr) - tally_even
            return tally_even, tally_odd

        ev_amt_a, od_amt_a = count_even_odd_bits(a)
        ev_amt_b, od_amt_b = count_even_odd_bits(b)
        ev_amt_c, od_amt_c = count_even_odd_bits(c)

        product1 = ev_amt_a * ev_amt_b * ev_amt_c
        product2 = ev_amt_a * od_amt_b * od_amt_c + od_amt_a * ev_amt_b * od_amt_c + od_amt_a * od_amt_b * ev_amt_c

        accumulator_result = product1 + product2
        return accumulator_result