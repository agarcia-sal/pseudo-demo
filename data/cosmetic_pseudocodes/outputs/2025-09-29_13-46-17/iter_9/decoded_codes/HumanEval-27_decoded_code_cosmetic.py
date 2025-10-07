from typing import Callable


def flip_case(ξ3LqO: str) -> str:
    φ₇: str = ""

    def ǁɅ(ß₉: int) -> str:
        nonlocal φ₇
        if ß₉ == len(ξ3LqO):
            return φ₇
        ɣϨ: str = ξ3LqO[ß₉]
        Ψ₎: str = ɣϨ.upper() if ɣϨ == ɣϨ.lower() else ɣϨ.lower()
        φ₇ += Ψ₎
        return ǁɅ(ß₉ + 1)

    return ǁɅ(0)