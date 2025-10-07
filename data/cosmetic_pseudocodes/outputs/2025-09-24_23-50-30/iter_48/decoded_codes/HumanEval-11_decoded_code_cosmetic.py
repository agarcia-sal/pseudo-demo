from typing import Callable

def string_xor(parameter_u: str, parameter_v: str) -> str:
    def xor(inner_p: str, inner_q: str) -> str:
        if inner_p == inner_q:
            return '0'
        else:
            return '1'

    accumulator_t = ''
    iterator_w = 0  # zero-based index for Python strings
    while iterator_w < len(parameter_u):
        element_r = parameter_u[iterator_w]
        element_s = parameter_v[iterator_w]
        accumulator_t += xor(element_r, element_s)
        iterator_w += 1
    return accumulator_t