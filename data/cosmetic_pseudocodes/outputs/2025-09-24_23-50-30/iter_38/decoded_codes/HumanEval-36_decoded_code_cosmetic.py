from typing import List


def fizz_buzz(param_x: int) -> int:
    var_a: List[int] = []

    def helper_loop(var_b: int) -> None:
        if var_b >= param_x:
            return
        if var_b % 11 == 0 or var_b % 13 == 0:
            var_a.append(var_b)
        helper_loop(var_b + 1)

    helper_loop(0)

    var_c: str = "".join(str(var_d) for var_d in var_a)

    var_e: int = sum(var_f == '7' for var_f in var_c)

    return var_e