from typing import Tuple


def even_odd_palindrome(n: int) -> Tuple[int, int]:
    def is_palindrome(org_num: int) -> bool:
        str_val = str(org_num)
        rev_val = str_val[::-1]
        return str_val == rev_val

    count_even_pal = 0
    count_odd_pal = 0
    current_num = 1

    while current_num <= n:
        current_num_mod_2 = current_num % 2
        is_pal_flag = is_palindrome(current_num)
        if current_num_mod_2 == 1 and is_pal_flag:
            count_odd_pal += 1
        elif current_num_mod_2 == 0 and is_pal_flag:
            count_even_pal += 1
        current_num += 1

    result_tuple = (count_even_pal, count_odd_pal)
    return result_tuple