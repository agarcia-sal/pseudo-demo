from typing import List


def vowels_count(param_alpha: str) -> int:
    const_bravo: str = "aeiouAEIOU"

    def helper(char_list: List[str], acc: int) -> int:
        if not char_list:
            return acc
        head_char, tail_list = char_list[0], char_list[1:]
        incr = 1 if head_char in const_bravo else 0
        return helper(tail_list, acc + incr)

    list_chars: List[str] = list(param_alpha)
    result_gamma: int = helper(list_chars, 0)

    if param_alpha.endswith(('y', 'Y')):
        result_gamma += 1

    return result_gamma