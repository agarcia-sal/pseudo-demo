from typing import Callable


def is_palindrome(input_string: str) -> bool:
    # foldr: fold from right, implemented via reversed iteration
    # building reversed string and comparing to input_string
    reversed_string = "".join(reversed(input_string))
    return input_string == reversed_string


def make_palindrome(input_string: str) -> str:
    length = len(input_string)

    def aux(ħ₁₀₇₉ξ: int) -> str:
        if ħ₁₀₇₉ξ >= length:
            return ""
        suffix = input_string[ħ₁₀₇₉ξ:]
        if not is_palindrome(suffix):
            return aux(ħ₁₀₇₉ξ + 1)
        else:
            prefix = input_string[:ħ₁₀₇₉ξ]
            reversed_prefix = "".join(reversed(prefix))
            return input_string + reversed_prefix

    return aux(0)