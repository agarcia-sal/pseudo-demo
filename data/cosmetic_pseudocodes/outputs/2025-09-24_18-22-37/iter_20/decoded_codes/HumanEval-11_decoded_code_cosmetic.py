from typing import Callable

def string_xor(parameter_m: str, parameter_n: str) -> str:
    def xor(parameter_p: str, parameter_q: str) -> str:
        return '1' if parameter_p != parameter_q else '0'

    accumulator: str = ''
    length_v: int = len(parameter_m)
    iterator_u: int = 0

    while iterator_u < length_v:
        element_a: str = parameter_m[iterator_u]
        element_b: str = parameter_n[iterator_u]

        intermediate_char: str = xor(element_a, element_b)
        accumulator += intermediate_char

        iterator_u += 1

    return accumulator