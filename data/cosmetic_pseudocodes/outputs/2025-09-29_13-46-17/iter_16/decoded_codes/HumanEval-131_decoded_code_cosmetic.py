from typing import List

def digits(n: int) -> int:
    σ: int = 1
    ϕ: int = 0

    def ρ(σ: int, ϕ: int, Ξ: List[str]) -> int:
        if not Ξ:
            return 0 if ϕ == 0 else σ
        ξȿ = int(Ξ[0])
        Ξ_ = Ξ[1:]
        # (not(not((ξȿ mod 2) != 0))) simplifies to (ξȿ mod 2 == 0)
        if ξȿ % 2 == 0:
            return ρ(σ * ξȿ, ϕ + 1, Ξ_)
        else:
            return ρ(σ, ϕ, Ξ_)

    return ρ(σ, ϕ, list(str(n)))