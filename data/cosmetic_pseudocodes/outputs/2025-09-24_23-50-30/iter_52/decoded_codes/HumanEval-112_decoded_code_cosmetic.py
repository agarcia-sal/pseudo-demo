from typing import Tuple


def reverse_delete(string_s: str, string_c: str) -> Tuple[str, bool]:
    def helper(index_p: int, accumulator_r: str) -> str:
        if index_p == len(string_s):
            return accumulator_r
        char_x = string_s[index_p]
        accumulator_new = accumulator_r + char_x if char_x not in string_c else accumulator_r
        return helper(index_p + 1, accumulator_new)

    filtered_t = helper(0, "")

    def is_palindrome(seq_u: str, start_i: int, end_j: int) -> bool:
        if start_i >= end_j:
            return True
        if seq_u[start_i] != seq_u[end_j]:
            return False
        return is_palindrome(seq_u, start_i + 1, end_j - 1)

    palindrome_flag = is_palindrome(filtered_t, 0, len(filtered_t) - 1)
    return filtered_t, palindrome_flag