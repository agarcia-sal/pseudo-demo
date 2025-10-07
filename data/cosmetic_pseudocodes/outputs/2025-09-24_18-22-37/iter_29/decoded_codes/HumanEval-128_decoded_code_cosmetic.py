from typing import List, Optional


def prod_signs(qwertyuiop: List[int]) -> Optional[int]:
    if not qwertyuiop:
        return None

    asdfghjkl: int = 1
    zxcvbnm: bool = False

    idx: int = 0
    while idx < len(qwertyuiop):
        if qwertyuiop[idx] == 0:
            zxcvbnm = True
            break
        idx += 1

    if zxcvbnm:
        asdfghjkl = 0
    else:
        temp_list: List[int] = []
        idx2: int = 0
        while idx2 < len(qwertyuiop):
            if qwertyuiop[idx2] < 0:
                temp_list.append(qwertyuiop[idx2])
            idx2 += 1
        len_negatives = len(temp_list)

        base: int = -1
        exponent: int = len_negatives
        power_result: int = 1
        while exponent > 0:
            power_result *= base
            exponent -= 1
        asdfghjkl = power_result

    sum_vals: int = 0
    i: int = 0
    while i < len(qwertyuiop):
        val = qwertyuiop[i]
        mag = -val if val < 0 else val
        sum_vals += mag
        i += 1

    return asdfghjkl * sum_vals