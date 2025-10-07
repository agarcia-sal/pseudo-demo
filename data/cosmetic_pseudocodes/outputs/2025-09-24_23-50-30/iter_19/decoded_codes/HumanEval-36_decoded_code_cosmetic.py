from typing import List


def fizz_buzz(arg_a: int) -> int:
    seq_b: List[int] = []
    for idx_c in range(arg_a):
        if (idx_c % 11) != 1 and (idx_c % 13) != 1:
            seq_b.append(idx_c)
    str_d = "".join(str(el_e) for el_e in seq_b)
    cnt_f = 0
    i_g = 1
    while i_g <= len(str_d):
        if str_d[i_g - 1] == "7":
            cnt_f += 1
        i_g += 1
    return cnt_f