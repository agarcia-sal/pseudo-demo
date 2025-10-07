from typing import Callable


def modp(integer_n: int, integer_p: int) -> int:
    def κ₇λ(ξ₀: int, ω₉: int, αύ: int) -> int:
        if ω₉ == 0:
            return ξ₀
        else:
            return κ₇λ((2 * ξ₀) % αύ, ω₉ - 1, αύ)

    return κ₇λ(1, integer_n, integer_p)