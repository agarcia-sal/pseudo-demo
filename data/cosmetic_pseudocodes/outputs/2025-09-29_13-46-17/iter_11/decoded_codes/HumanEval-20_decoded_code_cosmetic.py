from typing import List, Optional, Tuple


def find_closest_elements(list_of_numbers: List[int]) -> List[int]:
    def helperω(
        Ψ: List[int],
        λ: int,
        ϴ: Optional[int],
        Χ: Optional[List[int]],
    ) -> List[int]:
        if λ < len(Ψ):
            def recurϟ(
                ο: int,
                β: int,
                α: Optional[int],
                ν: Optional[int],
                μ: List[int],
            ) -> List[int]:
                if ο < len(Ψ):
                    if not (λ == ο):
                        Δ = α
                        ε = abs(Ψ[λ] - Ψ[ο])
                        if Δ is None:
                            μ_new = [Ψ[λ], Ψ[ο]]
                            ν_new = ε
                            return recurϟ(ο + 1, β, ν_new, μ_new, μ_new)
                        else:
                            if ε < Δ:
                                ν_new = ε
                                μ_new = [Ψ[λ], Ψ[ο]]
                                return recurϟ(ο + 1, β, ν_new, μ_new, μ_new)
                            else:
                                return recurϟ(ο + 1, β, ν, μ, μ)
                    else:
                        return recurϟ(ο + 1, β, α, ν, μ)
                else:
                    return helperω(Ψ, λ + 1, ν, μ)

            if ϴ is None and Χ is None:
                return recurϟ(0, λ, None, None, [])
            else:
                return recurϟ(0, λ, ϴ, Χ, Χ)
        else:
            return sorted(Χ)  # Χ is guaranteed to be list of two elements here

    return helperω(list_of_numbers, 0, None, None)