from typing import List, Tuple

class Solution:
    def tripletCount(self, a: List[int], b: List[int], c: List[int]) -> int:
        def count_even_odd_bits(arr: List[int]) -> Tuple[int, int]:
            def bit_counter_rec(index_val: int, ev_count_param: int) -> int:
                if not (index_val < len(arr)):
                    return ev_count_param
                current_number_temp = arr[index_val]
                bit_counter_temp = 0
                temp_val = current_number_temp
                while temp_val > 0:
                    bit_counter_temp += temp_val & 1
                    temp_val >>= 1
                is_even_bit_count = (bit_counter_temp & 1) == 0
                ev_count_next = ev_count_param
                if is_even_bit_count:
                    ev_count_next += 1
                return bit_counter_rec(index_val + 1, ev_count_next)

            total_len_var = len(arr)
            even_total = bit_counter_rec(0, 0)
            odd_total = total_len_var - even_total
            return even_total, odd_total

        ev_a, od_a = count_even_odd_bits(a)
        ev_b, od_b = count_even_odd_bits(b)
        ev_c, od_c = count_even_odd_bits(c)

        tmp_case_one_var = ev_a * ev_b
        first_case_full = tmp_case_one_var * ev_c

        case_two_part1 = ev_a * od_b * od_c
        case_two_part2 = od_a * ev_b * od_c
        case_two_part3 = od_a * od_b * ev_c
        case_two_combined = case_two_part1 + case_two_part2 + case_two_part3

        output_result = first_case_full + case_two_combined
        return output_result