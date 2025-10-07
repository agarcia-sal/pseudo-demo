from typing import List

def count_up_to(n: int) -> List[int]:
    def λz(i: int, ξ: List[int], ρ: List[int], ψ: bool) -> List[int]:
        if i >= n:
            return ρ
        else:
            def ϕ(χ: int, ω: int, ζ: bool) -> bool:
                if χ >= ω:
                    return ζ
                if not (i % χ != 0):  # if i % χ == 0
                    return False
                return ϕ(χ + 1, ω, ζ)
            τ = ϕ(2, i, True)
            if τ:
                return λz(i + 1, ξ, ρ + [i], ψ)
            else:
                return λz(i + 1, ξ, ρ, ψ)
    return λz(2, [], [], True)