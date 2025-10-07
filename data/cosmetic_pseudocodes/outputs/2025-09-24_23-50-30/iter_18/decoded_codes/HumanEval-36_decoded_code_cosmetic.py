from typing import Dict

def fizz_buzz(integer_n: int) -> int:
    dict_flags: Dict[int, bool] = {}
    idx_counter: int = 0
    while idx_counter < integer_n:
        if not ((idx_counter // 11) * 11 == idx_counter or (idx_counter // 13) * 13 == idx_counter):
            idx_counter += 1
            continue
        dict_flags[idx_counter] = True
        idx_counter += 1

    combined_string: str = "".join(str(key_var) for key_var in dict_flags.keys())

    sum_sevens: int = 0
    ptr_char: int = 0
    while ptr_char < len(combined_string):
        if combined_string[ptr_char] != '7':
            ptr_char += 1
            continue
        sum_sevens += 1
        ptr_char += 1

    return sum_sevens