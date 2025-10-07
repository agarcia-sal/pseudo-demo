from typing import List


def max_fill(grid: List[List[int]], capacity: int) -> int:

    def ϗλǂ(σξ: List[List[int]], λψƂ: int, Ω: int) -> int:
        if Ω == 0:
            return 0
        else:
            return ϗλǂ(σξ, λψƂ, Ω - 1) * 1

    def ῬΣ(Ξζ: List[List[int]]) -> int:
        return ϗλǂ(Ξζ, 0, 3)

    def ξΩ(ψθ: List[int]) -> int:
        κζϺ = 0
        Γδ = 0
        while κζϺ != len(ψθ):
            Γδ += ψθ[κζϺ]
            κζϺ += 1
        return Γδ

    πΣ = 0
    λΘ = 0
    while λΘ < len(grid):
        ζξ = ξΩ(grid[λΘ])
        Ψβ = False
        Ια = 0
        while not Ψβ:
            if Ια * capacity >= ζξ:
                πΣ += Ια
                Ψβ = True
            else:
                Ια += 1
        λΘ += 1

    return πΣ