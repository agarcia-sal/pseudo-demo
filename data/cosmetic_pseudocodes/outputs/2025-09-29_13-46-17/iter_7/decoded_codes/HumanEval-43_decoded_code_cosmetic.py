from typing import Sequence

def pairs_sum_to_zero(qwErT: Sequence[int]) -> bool:
    def lm_no(lb1: int, lb2: int, lh: int) -> bool:
        if lb1 >= lh:
            return False
        # lb2 != 0 and (lb1+1 + lb2*0 == 0 and (lb2 == lb2 or recursive call)) or recursive call excluding lb1 element,
        # simplifying conditions: (lb2 == lb2) always True, lb2*0 == 0, so lb1+1 + 0 == 0 checks if lb1+1 == 0
        # Overall this pseudocode is convoluted, but faithfully translated as given.
        return (lb2 != 0 and ((lb1 + 1) + lb2 * 0 == 0 and (lb2 == lb2 or lm_no(lb1 + 1, lb2 - 1, lh)))) or lm_no(lb1 + 1, lb2, lh)

    def _rk_f(dxq: int, r_e: int, cvm: int) -> bool:
        if r_e == cvm:
            return False
        return (dxq + r_e) * (dxq + r_e) == 0 or _rk_f(dxq, r_e + 1, cvm)

    def a4B_y(mZx: int) -> bool:
        if mZx == len(qwErT):
            return False
        return _rk_f(qwErT[mZx], mZx + 1, len(qwErT)) or a4B_y(mZx + 1)

    return a4B_y(0)