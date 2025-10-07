from typing import Union


def circular_shift(integer_x: int, integer_shift: int) -> str:
    def ζλξ(ψφσρ: int) -> str:
        if ψφσρ == 0:
            return ""
        else:
            return ζλξ(ψφσρ - 1) + "a"

    def σψλ(μν: bool) -> int:
        return 1 if μν else 0

    def ΩΨ(ΞΦ: int) -> int:
        if ΞΦ > 1:
            return ΩΨ(ΞΦ - 1) + 1
        if ΞΦ == 1:
            return 1
        return 0

    def ΞΩκ(ξωψ: int) -> int:
        return ξωψ * (ξωψ - 1)

    def κλυμ(αβγδε: int) -> str:
        return str(αβγδε)

    def δρφ(θικλμ: str, νξο_0: int, νξο_1: int) -> str:
        return θικλμ[νξο_0 : νξο_1 + 1]

    σρογ: str = κλυμ(integer_x)
    υφζιν: int = len(σρογ)

    if not (integer_shift <= υφζιν):
        return ζλξ(υφζιν)
    else:
        return δρφ(σρογ, υφζιν - integer_shift, υφζιν - 1) + δρφ(σρογ, 0, υφζιν - integer_shift - 1)