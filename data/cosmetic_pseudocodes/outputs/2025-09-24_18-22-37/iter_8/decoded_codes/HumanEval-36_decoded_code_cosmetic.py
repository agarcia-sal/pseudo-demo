from typing import List


def fizz_buzz(parameter_p: int) -> int:
    accumulator_q: int = 0  # unused as per pseudocode
    container_r: List[int] = []
    variable_s: int = 0

    while variable_s < parameter_p:
        interim_t: int = variable_s % 11
        interim_u: int = variable_s % 13

        if interim_t == 0 or interim_u == 0:
            container_r.append(variable_s)

        variable_s += 1

    holder_v: str = ""
    iterator_w: int = 0

    while iterator_w < len(container_r):
        element_x: int = container_r[iterator_w]
        holder_v += str(element_x)
        iterator_w += 1

    total_y: int = 0
    index_z: int = 0

    while index_z < len(holder_v):
        symbol_aa: str = holder_v[index_z]
        if symbol_aa == '7':
            total_y += 1
        index_z += 1

    return total_y