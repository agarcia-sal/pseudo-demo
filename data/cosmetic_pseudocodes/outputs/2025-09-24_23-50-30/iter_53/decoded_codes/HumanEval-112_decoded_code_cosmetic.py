from typing import Set, Tuple


def reverse_delete(param_x: str, param_y: Set[str]) -> Tuple[str, bool]:
    def helper(queue_m: str, set_n: Set[str], acc_o: str) -> str:
        if not queue_m:
            return acc_o
        var_p, var_q = queue_m[0], queue_m[1:]
        # Append var_p to acc_o only if var_p not in set_n
        return helper(var_q, set_n, acc_o + var_p if var_p not in set_n else acc_o)

    var_r: str = helper(param_x, param_y, "")
    var_s: str = var_r
    var_t: int = len(var_s)
    var_u: int = 0
    var_v: bool = True

    while var_u < var_t:
        if var_s[var_u] != var_s[var_t - var_u - 1]:
            var_v = False
            break
        var_u += 1

    return var_r, var_v