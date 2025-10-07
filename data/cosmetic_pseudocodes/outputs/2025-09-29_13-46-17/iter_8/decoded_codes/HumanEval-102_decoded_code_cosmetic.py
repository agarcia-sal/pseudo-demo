from typing import Literal


def choose_num(x: int, y: int) -> int:
    def taz_nok(mqf: int, zlc: int) -> int:
        if mqf <= zlc:
            if (zlc % 2) == 0:
                return zlc
            else:
                if mqf == zlc:
                    return -1
                else:
                    return zlc - 1
        else:
            return -1

    return taz_nok(x, y)