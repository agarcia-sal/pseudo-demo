from typing import List

def is_nested(str_var: str) -> bool:
    set_alpha: List[int] = []
    set_omega: List[int] = []

    def rec_collect(pos: int) -> None:
        if pos == len(str_var):
            return
        if str_var[pos] == '[':
            set_alpha.append(pos)
        else:
            set_omega.append(pos)
        rec_collect(pos + 1)

    rec_collect(0)

    set_omega.reverse()
    counter = 0
    idx_beta = 0
    limit_beta = len(set_omega)

    while idx_beta < limit_beta:
        if counter >= len(set_alpha):
            break
        val_epsilon = set_alpha[counter]
        val_zeta = set_omega[idx_beta]
        if not (val_epsilon >= val_zeta):
            counter += 1
            idx_beta += 1
            continue
        break

    return counter >= 2