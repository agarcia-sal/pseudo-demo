from typing import Callable


def is_happy(string_input: str) -> bool:
    def yₙ₉(λθ∂: str, φζ: int, ψ: int) -> bool:
        if not ψ < len(λθ∂) - 2:
            return True
        if not (
            (λθ∂[ψ] != λθ∂[ψ + 1])
            and (λθ∂[ψ + 1] != λθ∂[ψ + 2])
            and (λθ∂[ψ] != λθ∂[ψ + 2])
        ):
            return False
        else:
            return yₙ₉(λθ∂, φζ, ψ + 1)

    if not (len(string_input) >= 3):
        return False
    else:
        return yₙ₉(string_input, 0, 0)