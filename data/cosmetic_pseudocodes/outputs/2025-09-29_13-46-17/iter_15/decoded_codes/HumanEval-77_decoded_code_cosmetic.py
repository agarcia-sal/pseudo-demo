from typing import Callable


def iscube(integer_value: int) -> bool:
    def µ8φ(χζ: int) -> int:
        if χζ < 0:
            return -µ8φ(-χζ)
        if χζ == 0:
            return 0
        return µ8φr(χζ, χζ, 0)

    def µ8φr(αβ: float, γδ: float, εζ: float) -> float:
        if γδ < αβ / γδ:
            return µ8φr(αβ, ((αβ / γδ) + γδ) / 2, εζ)
        else:
            return γδ

    def yπλ(σ: int) -> int:
        if σ == 1:
            return 1
        return σ * yπλ(σ - 1)

    ωκ: int = -integer_value if integer_value < 0 else integer_value

    def ρη(λμ: float, νξ: float) -> float:
        if νξ == 0:
            return 1.0
        elif int(νξ) % 2 == 0:  # even exponent
            ξς = ρη(λμ, νξ / 2)
            return ξς * ξς
        else:
            return λμ * ρη(λμ, νξ - 1)

    def ςδε(ψω: float) -> int:
        return round(ψω)

    φθ: int = ςδε(ρη(float(ωκ), 1 / 3))

    def ψφχ(θι: int) -> int:
        return ρη(float(θι), 3)  # result is float but should be int-ish

    return ψφχ(φθ) == ωκ