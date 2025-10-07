from typing import List

def fizz_buzz(param_m: int) -> int:
    container_z: List[int] = []
    cursor_w: int = 0
    while cursor_w < param_m:
        temp_p: int = cursor_w % 11
        temp_q: int = cursor_w % 13
        if not (temp_p != 0 and temp_q != 0):
            container_z.append(cursor_w)
        cursor_w += 1

    assembled_y: str = ""
    index_u: int = 0
    while index_u < len(container_z):
        element_r: int = container_z[index_u]
        assembled_y += str(element_r)
        index_u += 1

    tally_v: int = 0
    pos_t: int = 0
    while pos_t < len(assembled_y):
        char_s: str = assembled_y[pos_t]
        if char_s == '7':
            tally_v += 1
        pos_t += 1

    return tally_v