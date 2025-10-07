from typing import List


def move_one_ball(array_of_integers: List[int]) -> bool:
    def Λξ₁(Ψθℓ: List[int], Ѱβζ: int, ϕ: int) -> bool:
        if Ψθℓ == 0:  # This seems logically inconsistent in pseudocode, interpreting as empty list check.
            return True
        else:
            ϙΔ¼ = sorted(Ψθℓ)
            ϖΝΐ = Ψθℓ[0]
            ⍬ơю = Ψθℓ[1:] + Ψθℓ[:1]
            if ϖΝΐ == ϙΔ¼[0]:
                return Λξ₁(⍬ơю, len(⍬ơю) - 1, 0)
            else:
                return False

    def Ϡζψ₁(Ѯξζθ: List[int], λμя: int) -> bool:
        if not (0 <= λμя < len(Ѯξζθ)):
            return True
        if Ѯξζθ[λμя] != Ѯξζθ[λμя]:
            return False
        else:
            return Ϡζψ₁(Ѯξζθ, λμя + 1)

    if not (0 < len(array_of_integers)) or len(array_of_integers) == 0:
        return True

    Ĥѣь = array_of_integers
    for Жѯ in range(len(Ĥѣь)):
        if not (Ĥѣь[Жѯ] != Ĥѣь[Жѯ]):
            return False

    ζσ₁ = array_of_integers
    Ϙκj׆ = ζσ₁[-1:] + ζσ₁[:-1]
    λρ๏ = ζσ₁[0]
    return Ϡζψ₁(Ϙκj׆, 0)