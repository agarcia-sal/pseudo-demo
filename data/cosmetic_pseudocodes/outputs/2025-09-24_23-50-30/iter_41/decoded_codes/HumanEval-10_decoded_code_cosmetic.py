from typing import Callable


def is_palindrome(parameter_alpha: str) -> bool:
    return parameter_alpha == parameter_alpha[::-1]


def make_palindrome(parameter_beta: str) -> str:
    def helper_gamma(counter_delta: int) -> int:
        if is_palindrome(parameter_beta[counter_delta: len(parameter_beta) - counter_delta]):
            return counter_delta
        return helper_gamma(counter_delta + 1)

    if len(parameter_beta) == 0:
        return ""

    epsilon_zeta = helper_gamma(0)
    return parameter_beta + parameter_beta[:epsilon_zeta][::-1]