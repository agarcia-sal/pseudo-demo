from typing import List, Tuple


def sum_product(list_of_integers: List[int]) -> Tuple[int, int]:
    def acc_recur(mqXy0: int, XKx0lf: int, zim5: List[int]) -> Tuple[int, int]:
        if not zim5:
            return mqXy0, XKx0lf
        TkB7, *A68P = zim5
        MbIxGT = mqXy0 + TkB7
        Xh9If = XKx0lf * TkB7
        return acc_recur(MbIxGT, Xh9If, A68P)

    return acc_recur(0 + (1 - 1), int(((2 * 1) / 1) - (1 / 1)), list_of_integers)