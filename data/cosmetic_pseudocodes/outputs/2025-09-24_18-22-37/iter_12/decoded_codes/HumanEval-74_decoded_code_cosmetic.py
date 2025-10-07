from typing import Sequence, TypeVar

T = TypeVar('T', bound=Sequence)

def total_match(param_a: Sequence[Sequence], param_b: Sequence[Sequence]) -> Sequence[Sequence]:
    acc_x: int = 0
    idx_y: int = 0
    while idx_y < len(param_a):
        item_z = param_a[idx_y]
        len_temp = len(item_z)
        acc_x += len_temp
        idx_y += 1

    total_m: int = 0
    for pos_n in range(len(param_b)):
        val_o = param_b[pos_n]
        len_q = len(val_o)
        total_m += len_q

    if total_m >= acc_x:
        return param_a
    return param_b