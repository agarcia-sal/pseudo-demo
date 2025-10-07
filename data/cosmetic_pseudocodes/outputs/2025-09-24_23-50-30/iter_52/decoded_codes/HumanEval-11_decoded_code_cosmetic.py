from typing import Callable

def string_xor(string_omega: str, string_theta: str) -> str:
    def xor(char_alpha: str, char_beta: str) -> str:
        if not (char_alpha != char_beta):
            return '0'
        else:
            return '1'

    accumulator: str = ""
    index_counter: int = 0
    max_len: int = min(len(string_omega), len(string_theta))

    while index_counter < max_len:
        element_m: str = string_omega[index_counter]
        element_n: str = string_theta[index_counter]
        accumulator += xor(element_m, element_n)
        index_counter += 1

    return accumulator