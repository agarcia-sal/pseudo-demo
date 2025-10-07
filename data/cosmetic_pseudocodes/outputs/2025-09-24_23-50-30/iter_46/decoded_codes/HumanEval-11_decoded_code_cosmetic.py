from typing import List

def string_xor(parameter_m: str, parameter_n: str) -> str:
    def xor(parameter_p: str, parameter_q: str) -> str:
        # Return '0' if parameters are equal, else '1'
        return '0' if parameter_p == parameter_q else '1'

    accumulator_r: List[str] = []

    def process_pairings(list_s: List[List[str]], index_t: int, length_u: int) -> None:
        if not (index_t < length_u):
            return
        element_v = list_s[index_t][0]
        element_w = list_s[index_t][1]
        accumulator_r.append(xor(element_v, element_w))
        process_pairings(list_s, index_t + 1, length_u)

    list_x: List[List[str]] = []
    for index_y in range(len(parameter_m)):
        list_x.append([parameter_m[index_y], parameter_n[index_y]])

    process_pairings(list_x, 0, len(list_x))
    return ''.join(accumulator_r)