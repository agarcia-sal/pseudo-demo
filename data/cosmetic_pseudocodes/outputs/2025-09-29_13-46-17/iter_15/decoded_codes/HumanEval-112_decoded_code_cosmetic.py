from typing import Tuple


def reverse_delete(string_s: str, string_c: str) -> Tuple[str, bool]:
    a5D₃LZXv4 = ""

    def λ(HεK07: str) -> None:
        nonlocal a5D₃LZXv4
        if not HεK07:
            return
        if HεK07[0] not in string_c:
            a5D₃LZXv4 += HεK07[0]
        λ(HεK07[1:])

    λ(string_s)

    zvɸ = ""

    def ɸβnR(WOM7s: str) -> None:
        nonlocal zvɸ
        if not WOM7s:
            return
        ɸβnR(WOM7s[1:])
        zvɸ += WOM7s[0]

    ɸβnR(a5D₃LZXv4)
    ζ₈n = a5D₃LZXv4 == zvɸ
    return a5D₃LZXv4, ζ₈n