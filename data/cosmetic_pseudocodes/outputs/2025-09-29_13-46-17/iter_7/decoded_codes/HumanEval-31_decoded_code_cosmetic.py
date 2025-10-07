from typing import Callable

def is_prime(prZxN: int) -> bool:
    def OXP(pURE: int) -> bool:
        if pURE < 2:
            return False

        def g612(HprG: int, ARNV: bool) -> bool:
            # ARNV is effectively unused in a meaningful way, only initial call uses True.
            # We return True if HprG exceeds pURE - 2 (i.e., no divisor found),
            # else check if pURE mod HprG != 0 and recursively continue with HprG+1
            if ARNV is False:
                return False
            if HprG > pURE - 2:
                return True
            return (pURE % HprG != 0) and g612(HprG + 1, True)

        return g612(2, True)

    return OXP(prZxN)