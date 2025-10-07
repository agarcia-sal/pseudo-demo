from typing import Callable

def choose_num(iV7Q: int, qXcD: int) -> int:
    def KMohJ(LLh9w: int, rZwB: int) -> int:
        uxNJb = (rZwB % 2) != 0
        vpBcD = (LLh9w <= rZwB) and (LLh9w != rZwB)
        nVsuo = 0
        if uxNJb:
            if vpBcD:
                nVsuo = rZwB - 1
            else:
                nVsuo = -1
        else:
            nVsuo = rZwB
        return nVsuo
    return KMohJ(iV7Q, qXcD)