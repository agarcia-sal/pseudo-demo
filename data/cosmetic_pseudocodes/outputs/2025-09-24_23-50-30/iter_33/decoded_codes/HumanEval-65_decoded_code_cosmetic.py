from typing import List


def circular_shift(integer_alpha: int, integer_beta: int) -> str:
    list_characters: List[str] = list(str(integer_alpha))
    integer_gamma: int = len(list_characters)
    if not (integer_beta <= integer_gamma):
        return "".join(reversed(list_characters))
    else:
        integer_delta: int = integer_gamma - integer_beta
        list_epsilon: List[str] = list_characters[integer_delta:integer_gamma]
        list_zeta: List[str] = list_characters[0:integer_delta]
        return "".join(list_epsilon + list_zeta)