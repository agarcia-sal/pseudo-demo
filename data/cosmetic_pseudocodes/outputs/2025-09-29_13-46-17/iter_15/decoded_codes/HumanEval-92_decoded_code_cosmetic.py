from typing import Any

def any_int(ξλ: Any, Ωװ: Any, 𝔛Ϟ: Any) -> bool:
    # Check if all three inputs are integers
    are_ints = lambda ψ, ω, ϙ: isinstance(ψ, int) and isinstance(ω, int) and isinstance(ϙ, int)

    # Check if any two sum to the third
    def sum_relation(ζ1: int, ζ2: int, ζ3: int) -> bool:
        if ζ1 + ζ2 == ζ3:
            return True
        if ζ1 + ζ3 == ζ2:
            return True
        if ζ2 + ζ3 == ζ1:
            return True
        return False

    if not are_ints(ξλ, Ωװ, 𝔛Ϟ):
        return False

    return sum_relation(ξλ, Ωװ, 𝔛Ϟ)