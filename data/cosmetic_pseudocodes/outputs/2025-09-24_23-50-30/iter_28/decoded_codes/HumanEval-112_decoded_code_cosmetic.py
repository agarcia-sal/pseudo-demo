from typing import Tuple

def reverse_delete(string_s: str, string_c: str) -> Tuple[str, bool]:
    def filter_chars(index_a: int, accum_b: str) -> str:
        if index_a == len(string_s):
            return accum_b
        current_d = string_s[index_a]
        not_in_e = current_d not in string_c
        next_accum_f = accum_b + (current_d if not_in_e else "")
        return filter_chars(index_a + 1, next_accum_f)

    filtered_g = filter_chars(0, "")
    reversed_h = "".join(filtered_g[i] for i in range(len(filtered_g) - 1, -1, -1))
    is_palindrome_i = reversed_h == filtered_g
    return filtered_g, is_palindrome_i