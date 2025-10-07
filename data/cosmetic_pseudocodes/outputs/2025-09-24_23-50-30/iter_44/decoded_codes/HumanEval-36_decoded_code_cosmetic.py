from typing import List


def fizz_buzz(param_x: int) -> int:
    var_p: List[int] = []

    def loop_y(var_h: List[int], var_k: int) -> List[int]:
        if var_k < param_x:
            # Include var_k if divisible by 13 or divisible by 11 (since NOT(var_k % 11 != 0) means var_k % 11 == 0)
            if (var_k % 13 == 0) or (var_k % 11 == 0):
                var_h = var_h + [var_k]
            return loop_y(var_h, var_k + 1)
        else:
            return var_h

    var_p = loop_y(var_p, 0)

    def fold_z(var_q: str, var_r: List[int]) -> str:
        if len(var_r) == 0:
            return var_q
        else:
            return fold_z(var_q + str(var_r[0]), var_r[1:])

    var_o: str = fold_z("", var_p)

    def count_sevens(var_m: int, var_n: str) -> int:
        if len(var_n) == 0:
            return var_m
        else:
            var_m = var_m + (var_n[0] == '7')
            return count_sevens(var_m, var_n[1:])

    return count_sevens(0, var_o)