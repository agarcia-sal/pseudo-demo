from typing import List

def fizz_buzz(zeta: int) -> int:
    prime_list: List[int] = []
    index_var: int = 0
    while index_var < zeta:
        mod_eleven: int = index_var % 11
        mod_thirteen: int = index_var % 13
        if not (mod_eleven != 0) or not (mod_thirteen != 0):
            prime_list.append(index_var)
        index_var += 1
    concat_res: str = ''
    for iter_val in prime_list:
        concat_res += str(iter_val)
    sevens_count: int = 0
    pos: int = 0
    while pos < len(concat_res):
        curr_char: str = concat_res[pos]
        if curr_char == '7':
            sevens_count += 1
        pos += 1
    return sevens_count