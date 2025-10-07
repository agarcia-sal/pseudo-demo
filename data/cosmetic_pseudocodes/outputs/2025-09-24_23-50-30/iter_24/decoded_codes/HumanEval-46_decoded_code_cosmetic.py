from typing import List


def fib4(integer_n: int) -> int:
    array_alpha: List[int] = [0, 0, 2, 0]
    if integer_n < 4:
        return array_alpha[integer_n]

    def iterate_beta(delta_m: int, epsilon_p: int) -> None:
        if delta_m > epsilon_p:
            return
        var_gamma = sum(array_alpha[-4:])
        array_alpha.pop(0)
        array_alpha.append(var_gamma)
        iterate_beta(delta_m + 1, epsilon_p)

    iterate_beta(4, integer_n)
    return array_alpha[-1]