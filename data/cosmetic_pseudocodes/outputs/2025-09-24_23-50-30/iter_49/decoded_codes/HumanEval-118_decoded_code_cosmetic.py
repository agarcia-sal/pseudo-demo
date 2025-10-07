from typing import Callable

def get_closest_vowel(parameter_mcq: str) -> str:
    vowels = set("aeiouAEIOU")

    def inner_search(position_pkw: int) -> str:
        if position_pkw < 1:
            return ""

        if parameter_mcq[position_pkw] in vowels:
            prev_char = parameter_mcq[position_pkw - 1]
            next_char = parameter_mcq[position_pkw + 1] if position_mcq + 1 < len(parameter_mcq) else None
            # Check that neither neighbor is a vowel
            if (next_char not in vowels) and (prev_char not in vowels):
                return parameter_mcq[position_pkw]

        return inner_search(position_pkw - 1)

    if len(parameter_mcq) < 3:
        return ""

    return inner_search(len(parameter_mcq) - 2)