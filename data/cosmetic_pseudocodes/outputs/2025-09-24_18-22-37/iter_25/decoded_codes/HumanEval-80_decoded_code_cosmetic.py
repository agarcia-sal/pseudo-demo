from typing import Sequence

def is_happy(param_zeta: Sequence[str]) -> bool:
    total_length: int = len(param_zeta)
    if total_length < 3:
        return False

    pointer_alpha: int = 0
    while pointer_alpha <= total_length - 3:
        ch_m = param_zeta[pointer_alpha]
        ch_n = param_zeta[pointer_alpha + 1]
        ch_o = param_zeta[pointer_alpha + 2]

        cond1 = (ch_m == ch_n)
        cond2 = (ch_n == ch_o)
        cond3 = (ch_m == ch_o)

        if cond1 or cond2 or cond3:
            return False

        pointer_alpha += 1

    return True