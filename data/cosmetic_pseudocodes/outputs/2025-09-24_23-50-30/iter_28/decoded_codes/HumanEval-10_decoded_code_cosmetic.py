from typing import Callable

def is_palindrome(parameter_alpha: str) -> bool:
    return parameter_alpha == parameter_alpha[::-1]

def make_palindrome(parameter_beta: str) -> str:
    if len(parameter_beta) == 0:
        return ""
    def check_suffix(counter_delta: int) -> int:
        if is_palindrome(parameter_beta[counter_delta:]):
            return counter_delta
        return check_suffix(counter_delta + 1)
    index_gamma: int = check_suffix(0)
    return parameter_beta + parameter_beta[:index_gamma][::-1]