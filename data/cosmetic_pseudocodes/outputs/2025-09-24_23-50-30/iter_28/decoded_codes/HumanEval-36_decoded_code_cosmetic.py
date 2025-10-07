from typing import List


def fizz_buzz(integer_n: int) -> int:
    def collect_divisible(accumulator_a: List[int], index_b: int, limit_c: int) -> List[int]:
        if index_b == limit_c:
            return accumulator_a
        divisible_by_11 = (index_b % 11 == 0)
        divisible_by_13 = (index_b % 13 == 0)
        if divisible_by_11 or divisible_by_13:
            return collect_divisible(accumulator_a + [index_b], index_b + 1, limit_c)
        return collect_divisible(accumulator_a, index_b + 1, limit_c)

    sequence_d = collect_divisible([], 0, integer_n)

    def accumulate_string(source_list_e: List[int], index_f: int, acc_str_g: str) -> str:
        if index_f == len(source_list_e):
            return acc_str_g
        return accumulate_string(source_list_e, index_f + 1, acc_str_g + str(source_list_e[index_f]))

    concatenation_h = accumulate_string(sequence_d, 0, "")

    def count_char_occurrences(text_i: str, position_j: int, target_k: str, tally_l: int) -> int:
        if position_j == len(text_i):
            return tally_l
        is_match_m = (text_i[position_j] == target_k)
        return count_char_occurrences(text_i, position_j + 1, target_k, tally_l + (1 if is_match_m else 0))

    return count_char_occurrences(concatenation_h, 0, '7', 0)