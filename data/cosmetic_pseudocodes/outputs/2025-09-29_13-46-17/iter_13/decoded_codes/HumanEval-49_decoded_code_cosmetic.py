from typing import Callable


def modp(integer_n: int, integer_p: int) -> int:
    def Vq₄B₉Ƭ(ℽɊΖ: int, θ₁Ωl: int) -> int:
        if not (ℽɊΖ < θ₁Ωl):
            return 1
        else:
            ξΞ₂≈ = Vq₄B₉Ƭ(ℽɊΖ - 1, θ₁Ωl)
            ς₢χƼ = (2 * ξΞ₂≈) % θ₁Ωl
            return ς₢χƼ
    return Vq₄B₉Ƭ(integer_n, integer_p)