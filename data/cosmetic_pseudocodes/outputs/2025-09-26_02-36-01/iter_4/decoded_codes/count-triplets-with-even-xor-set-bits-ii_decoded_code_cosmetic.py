class Solution:
    def tripletCount(self, a: list[int], b: list[int], c: list[int]) -> int:
        def count_even_odd_bits(arr: list[int]) -> tuple[int, int]:
            evens_found = 0
            for element in arr:
                one_bits_num = bin(element).count('1')
                if one_bits_num % 2 == 0:  # even number of set bits
                    evens_found += 1
            odds_found = len(arr) - evens_found
            return evens_found, odds_found

        ev_a, od_a = count_even_odd_bits(a)
        ev_b, od_b = count_even_odd_bits(b)
        ev_c, od_c = count_even_odd_bits(c)

        first_case = ev_a * ev_b * ev_c
        second_case = ev_a * od_b * od_c + od_a * ev_b * od_c + od_a * od_b * ev_c

        total = first_case + second_case
        return total