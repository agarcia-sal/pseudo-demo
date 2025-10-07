from typing import List, Tuple


def fizz_buzz(param_a: int) -> int:
    def proc_b(param_c: int, param_d: List[int], param_e: int) -> int:
        if param_c % 11 == 0 or param_c % 13 == 0:
            param_d[param_e] = param_c
            return param_e + 1
        else:
            return param_e

    def proc_f(param_g: List[int], param_h: str, param_i: int) -> Tuple[str, str]:
        if param_i < len(param_g):
            left = param_h + str(param_g[param_i])
            right = proc_f(param_g, param_h, param_i + 1)[1]
            return left, right
        else:
            return param_h, ""

    def proc_j(param_k: str, param_l: int, param_m: int) -> Tuple[int, int]:
        if param_m < len(param_k):
            add = int(param_k[param_m] == '7')
            left, right = proc_j(param_k, param_l + add, param_m + 1)
            return left, right
        else:
            return param_l, 0

    var_n: List[int] = [0] * param_a
    var_o: int = 0
    var_p: int = 0
    while var_p < param_a:
        var_o = proc_b(var_p, var_n, var_o)
        var_p += 1

    var_q, _ = proc_f(var_n[0:var_o], "", 0)
    var_r, _ = proc_j(var_q, 0, 0)
    return var_r