def string_xor(parameter_m: str, parameter_n: str) -> str:
    def xor(parameter_p: str, parameter_q: str) -> str:
        return '0' if parameter_p == parameter_q else '1'

    container_s: str = ''
    iterator_u: int = 0
    while iterator_u < len(parameter_m):
        container_s += xor(parameter_m[iterator_u], parameter_n[iterator_u])
        iterator_u += 1
    return container_s