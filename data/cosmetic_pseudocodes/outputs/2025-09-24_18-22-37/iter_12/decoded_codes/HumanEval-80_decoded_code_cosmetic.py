from typing import Sequence


def is_happy(param_x: Sequence[str]) -> bool:
    if len(param_x) < 3:
        return False

    for aux_i in range(len(param_x) - 2):
        val_a = param_x[aux_i]
        val_b = param_x[aux_i + 1]
        val_c = param_x[aux_i + 2]

        if val_a == val_b or val_b == val_c or val_a == val_c:
            return False

    return True