class Solution:
    def tripletCount(self, a: list[int], b: list[int], c: list[int]) -> int:
        def count_even_odd_bits(arr: list[int]) -> tuple[int, int]:
            total_evens = 0
            for num in arr:
                bit_ones = 0
                temp = num
                while temp > 0:
                    bit_ones += temp & 1
                    temp >>= 1
                if (bit_ones & 1) == 0:
                    total_evens += 1
            total_odds = len(arr) - total_evens
            return total_evens, total_odds

        even_a, odd_a = count_even_odd_bits(a)
        even_b, odd_b = count_even_odd_bits(b)
        even_c, odd_c = count_even_odd_bits(c)

        product_even_all = even_a * even_b * even_c
        aggregate_case2 = (even_a * odd_b * odd_c +
                           odd_a * even_b * odd_c +
                           odd_a * odd_b * even_c)

        final_count = product_even_all + aggregate_case2
        return final_count