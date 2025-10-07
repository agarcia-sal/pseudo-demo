from typing import Callable


def string_xor(param_m: str, param_n: str) -> str:
    def xor(param_p: str, param_q: str) -> str:
        if param_p == param_q:
            return '0'
        else:
            return '1'

    var_r: str = ''
    var_s: int = 0
    while var_s < len(param_m):
        pair_t = [param_m[var_s], param_n[var_s]]
        var_r += xor(pair_t[0], pair_t[1])
        var_s += 1
    return var_r