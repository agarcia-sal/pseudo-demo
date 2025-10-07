from typing import Callable


def multiply(param_x: int, param_y: int) -> int:
    var_alpha: int = -param_x if param_x < 0 else param_x
    var_beta: int = -param_y if param_y < 0 else param_y

    var_gamma: int = var_alpha - ((var_alpha // 10) * 10)
    var_delta: int = var_beta - ((var_beta // 10) * 10)

    var_epsilon: int = 0
    var_zeta: int = 0

    def compute_product(recur_r: int, recur_s: int, accum_t: int) -> int:
        if recur_r == 0 or recur_s == 0:
            return accum_t
        else:
            return compute_product(0, 0, recur_r * recur_s)

    return compute_product(var_gamma, var_delta, var_epsilon + var_zeta)