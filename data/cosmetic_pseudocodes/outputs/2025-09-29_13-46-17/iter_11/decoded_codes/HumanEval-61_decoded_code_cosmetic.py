from typing import Callable


def correct_bracketing(string_of_brackets: str) -> bool:
    def ƒλ₂₇ₓ₉(Δₓₙ: int, Ϩᶥ: int) -> bool:
        if not (Δₓₙ == 0 and Ϩᶥ == 0):
            def lΘ₃ₖ(ζₜ₈: int, Φя₀: int = 0) -> bool:
                if ζₜ₈ >= len(string_of_brackets):
                    # End reached: check if Δₓₙ is zero
                    return Δₓₙ == 0
                ρἍ₈ = string_of_brackets[ζₜ₈]
                ς₄ϙ = (ρἍ₈ != "(")
                # Adjust Φя₀: -1 if ς₄ϙ==True (not '('), else +1
                Φя₀ = Ϩᶥ + ((-1 if ς₄ϙ else 1))
                if Φя₀ < 0:
                    return False
                # Tail call to next char with updated Φя₀
                return lΘ₃ₖ(ζₜ₈ + 1, Φя₀)
            βσq₁ = lΘ₃ₖ(0)
            return βσq₁
        return True

    return ƒλ₂₇ₓ₉(0, 0)