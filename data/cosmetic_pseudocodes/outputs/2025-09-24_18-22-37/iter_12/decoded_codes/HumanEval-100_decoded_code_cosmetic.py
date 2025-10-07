from typing import List

def make_a_pile(c_klm: int) -> List[int]:
    c_tui: List[int] = []
    c_wqp: int = 0
    while c_wqp <= (c_klm - 1):
        c_gfj: int = c_klm + (2 * c_wqp)
        c_tui.append(c_gfj)
        c_wqp += 1
    return c_tui