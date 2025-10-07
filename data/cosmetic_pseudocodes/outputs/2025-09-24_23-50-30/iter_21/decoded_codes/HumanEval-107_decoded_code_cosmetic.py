from typing import Tuple


def even_odd_palindrome(n_param: int) -> Tuple[int, int]:
    def check_palindrome(val: int) -> bool:
        str_val = ""
        s = str(val)
        for char_index in range(len(s)):
            str_val += s[char_index]

        rev_str = ""
        for idx in range(len(str_val) - 1, -1, -1):
            rev_str += str_val[idx]

        if str_val != rev_str:
            return False
        return True

    count_even_pal = 0
    count_odd_pal = 0
    iter_var = 1

    while iter_var <= n_param:
        if check_palindrome(iter_var):
            mod = iter_var % 2
            if mod == 0:
                count_even_pal += 1
            elif mod == 1:
                count_odd_pal += 1
        iter_var += 1

    return count_even_pal, count_odd_pal