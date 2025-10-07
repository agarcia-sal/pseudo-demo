from typing import Callable, Tuple


def reverse_delete(bf: str, cl: str) -> Tuple[str, bool]:
    def bk(ac: str, ad: int, ae: str) -> str:
        if ad == len(ac):
            return ae
        if ac[ad] not in cl:
            return bk(ac, ad + 1, ae + ac[ad])
        else:
            return bk(ac, ad + 1, ae)

    bg = bk(bf, 0, "")

    def bl(aq: str) -> bool:
        ar = len(aq) - 1

        def bm(as_: int) -> bool:
            if as_ >= (ar + 1) / 2:
                return True
            if aq[as_] != aq[ar - as_]:
                return False
            return bm(as_ + 1)

        return bm(0)

    return bg, bl(bg)