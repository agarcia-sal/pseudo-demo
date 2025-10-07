from typing import NoReturn


def is_palindrome(variation_alpha: str) -> bool:
    reverse_version: str = ""
    position_beta: int = len(variation_alpha) - 1

    while position_beta >= 0:
        reverse_version += variation_alpha[position_beta]
        position_beta -= 1

    return reverse_version == variation_alpha


def make_palindrome(series_theta: str) -> str:
    if len(series_theta) == 0:
        return ""

    index_varphi: int = 0
    condition_met: bool = False

    while not condition_met:
        sub_part: str = series_theta[index_varphi:]
        condition_met = is_palindrome(sub_part)
        if not condition_met:
            index_varphi += 1

    prefix_part: str = series_theta[:index_varphi]
    reverse_prefix: str = ""
    iterator_gamma: int = len(prefix_part) - 1

    while iterator_gamma >= 0:
        reverse_prefix += prefix_part[iterator_gamma]
        iterator_gamma -= 1

    result_string: str = series_theta + reverse_prefix
    return result_string