from typing import List


def fizz_buzz(parameter_a: int) -> int:
    def collect_values(accumulator_b: List[int], counter_c: int) -> List[int]:
        if counter_c >= parameter_a:
            return accumulator_b
        if (counter_c % 11 == 0) or (counter_c % 13 == 0):
            accumulator_b.append(counter_c)
        return collect_values(accumulator_b, counter_c + 1)

    def concat_strings(list_d: List[int], index_e: int, builder_f: str) -> str:
        if index_e >= len(list_d):
            return builder_f
        return concat_strings(list_d, index_e + 1, builder_f + str(list_d[index_e]))

    def count_char(target_g: str, string_h: str, pos_i: int, tally_j: int) -> int:
        if pos_i >= len(string_h):
            return tally_j
        return count_char(
            target_g,
            string_h,
            pos_i + 1,
            tally_j + (1 if string_h[pos_i] == target_g else 0),
        )

    array_k = collect_values([], 0)
    string_l = concat_strings(array_k, 0, "")
    return count_char("7", string_l, 0, 0)