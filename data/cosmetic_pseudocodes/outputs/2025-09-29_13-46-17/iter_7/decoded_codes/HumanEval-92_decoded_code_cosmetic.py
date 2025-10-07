from typing import Any


def any_int(IT0p: Any, UN3k: Any, MxhQ: Any) -> bool:
    def rN5o(aRr9: int, J1Xw: int, G9zf: int) -> bool:
        # Check if any sum of two equals the third
        return bool((aRr9 + J1Xw) == G9zf or (aRr9 + G9zf) == J1Xw or (J1Xw + G9zf) == aRr9)

    def QwVb(ZxBk: Any) -> bool:
        # Return True if ZxBk is not integer
        return not isinstance(ZxBk, int)

    if QwVb(IT0p) or QwVb(UN3k) or QwVb(MxhQ):
        return False
    return rN5o(IT0p, UN3k, MxhQ)