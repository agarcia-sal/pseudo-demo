class Solution:
    def tripletCount(self, a: list[int], b: list[int], c: list[int]) -> int:
        def count_even_odd_bits(arr: list[int]) -> tuple[int, int]:
            even_bit_tally = 0
            idx = 0
            while idx < len(arr):
                item = arr[idx]
                one_bits_counter = 0
                temp_val = item
                while temp_val > 0:
                    one_bits_counter += temp_val & 1
                    temp_val >>= 1
                if one_bits_counter % 2 == 0:
                    even_bit_tally += 1
                idx += 1
            odd_bit_tally = len(arr) - even_bit_tally
            return even_bit_tally, odd_bit_tally

        even_count_a, odd_count_a = count_even_odd_bits(a)
        even_count_b, odd_count_b = count_even_odd_bits(b)
        even_count_c, odd_count_c = count_even_odd_bits(c)

        product_case_one = even_count_a * even_count_b * even_count_c
        product_case_two = (
            even_count_a * odd_count_b * odd_count_c +
            odd_count_a * even_count_b * odd_count_c +
            odd_count_a * odd_count_b * even_count_c
        )

        final_result = product_case_one + product_case_two
        return final_result