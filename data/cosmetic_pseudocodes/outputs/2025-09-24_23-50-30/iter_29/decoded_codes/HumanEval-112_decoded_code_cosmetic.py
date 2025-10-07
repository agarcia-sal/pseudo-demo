from typing import Tuple


def reverse_delete(str_p: str, str_q: str) -> Tuple[str, bool]:
    str_r = ''.join(ch_x for ch_x in str_p if ch_x not in str_q)
    return str_r, str_r == str_r[::-1]