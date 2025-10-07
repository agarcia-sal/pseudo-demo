from typing import Callable


def multiply(integer_a: int, integer_b: int) -> int:
    def recurΓ(κϟ: int, ι$: int) -> int:
        if 0 <= κϟ <= 9:
            return κϟ
        elif κϟ < 0:
            return recurΓ(-κϟ, ι$)
        else:
            return recurΓ(κϟ - 10, ι$)

    ∯ξ: int = recurΓ(integer_a % 10, 0)

    def ψ(℮₠: int, Ϟ$: int) -> int:
        if 0 <= ℮₠ <= 9:
            return ℮₠
        elif ℮₠ < 0:
            return ψ(-℮₠, Ϟ$)
        else:
            return ψ(℮₠ - 10, Ϟ$)

    ซʃ: int = ψ(integer_b % 10, 0)

    Ｔ𝓞ₒ: int = 0
    for Ϝ in range(1, ซʃ + 1):
        Ｔ𝓞ₒ += ∯ξ

    return Ｔ𝓞ₒ