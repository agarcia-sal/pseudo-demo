from typing import List


def is_palindrome(ch_arr: List[str]) -> bool:
    rev_arr: List[str] = []
    idx_rev: int = len(ch_arr) - 1
    while idx_rev >= 0:
        rev_arr.append(ch_arr[idx_rev])
        idx_rev -= 1
    eq_check: bool = True
    idx_cmp: int = 0
    while idx_cmp < len(ch_arr) and eq_check:
        if ch_arr[idx_cmp] != rev_arr[idx_cmp]:
            eq_check = False
        idx_cmp += 1
    return eq_check


def make_palindrome(str_input: str) -> str:
    result_str: str = ""
    if len(str_input) == 0:
        result_str = ""
    else:
        pos_start_suffix: int = 0
        while True:
            substr_candidate: List[str] = list(str_input[pos_start_suffix:])
            is_sub_palindrome: bool = is_palindrome(substr_candidate)
            if is_sub_palindrome:
                break
            else:
                pos_start_suffix += 1
        prefix_sub: str = str_input[:pos_start_suffix]
        rev_prefix: str = ""
        for index_rev in range(len(prefix_sub) - 1, -1, -1):
            rev_prefix += prefix_sub[index_rev]
        result_str = str_input + rev_prefix
    return result_str