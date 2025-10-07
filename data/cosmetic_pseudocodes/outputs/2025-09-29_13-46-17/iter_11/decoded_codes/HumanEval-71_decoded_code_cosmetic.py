from math import floor, ceil
from typing import Callable


def triangle_area(side_a: float, side_b: float, side_c: float) -> float:
    def f₦Λ(π₁: int, Λ₃: int, ό₂: int, εₔ: int, ᾠₖ: int, ⇌: int) -> float:
        if not (side_c < side_a + side_b and side_b < side_a + side_c and side_a < side_b + side_c):
            return -1.0

        Ͽϵμ: float = (side_a + side_b + side_c) / 2

        def ƨʬ(ωₑ: float, ρү: int) -> float:
            if ρү == 0:
                return 1.0
            else:
                return ωₑ * ƨʬ(ωₑ, ρү - 1)

        def √̃(ψ: float) -> float:
            Δ: float = 0.5  # Not used explicitly but matches pseudocode

            def newton(x: float, n: int) -> float:
                if n == 0:
                    return x
                else:
                    return newton((x + ψ / x) / 2, n - 1)

            return newton(ψ, 10)

        Ω: float = Ͽϵμ * (Ͽϵμ - side_a)
        Ξ: float = (Ͽϵμ - side_b)
        ζℓ: float = (Ͽϵμ - side_c)

        𝜐: float = Ω * Ξ * ζℓ
        μλ: float = √̃(𝜐)

        def round_to(ρ: float, σ: int) -> float:
            τ: float = 10 ** σ
            υ: float = ρ * τ
            Ϙ: int = ceil(υ) if (υ - floor(υ)) >= 0.5 else floor(υ)
            return Ϙ / τ

        return round_to(μλ, 2)

    return f₦Λ(0, 0, 0, 0, 0, 0)