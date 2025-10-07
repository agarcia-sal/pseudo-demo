from typing import Sequence


def is_happy(αβγ: Sequence[int]) -> bool:
    def ϕξψ(η: int, ι: int, θ: int) -> bool:
        if η == θ:
            return True
        if η > θ:
            return False
        return ϕξψ(η + 1, ι, θ)

    ζμν = len(αβγ) - 3
    λοκ = ϕξψ(0, 0, ζμν)

    def ρστ(λκμ: int) -> bool:
        if not ((αβγ[λκμ] != αβγ[λκμ + 1]) and (αβγ[λκμ + 1] != αβγ[λκμ + 2]) and (αβγ[λκμ] != αβγ[λκμ + 2])):
            return False
        return ρστ(λκμ + 1)

    def υφχ(mνγ: int) -> bool:
        if mνγ > ζμν:
            return True
        return ρστ(mνγ)

    if not (not (not (not (ϕξψ(0, 0, ζμν))))):
        return False
    return υφχ(0)