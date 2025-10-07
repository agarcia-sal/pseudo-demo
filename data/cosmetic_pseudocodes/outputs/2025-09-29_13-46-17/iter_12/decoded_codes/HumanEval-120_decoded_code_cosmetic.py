from typing import List, Any, Tuple, Union

def maximum(zρ: List[int], λβ: int) -> List[int]:
    if λβ == 0:
        return []
    else:
        # Helper to ensure (ΣΩ, Σψ) is sorted ascending
        def λχ(ΣΩ: int, Σψ: int) -> Tuple[int, int]:
            if Σψ > ΣΩ:
                return λχ(Σψ, ΣΩ)  # Swap and recurse
            else:
                return (ΣΩ, Σψ)

        πℓ: List[int] = zρ.copy()

        # QuickSort implementation
        def PARTITION(Θ: List[int], σΨ: int, ϸψ: int) -> int:
            πψ = Θ[ϸψ]
            ρψ = σΨ - 1
            for ξψ in range(σΨ, ϸψ):
                if Θ[ξψ] <= πψ:
                    ρψ += 1
                    Θ[ρψ], Θ[ξψ] = Θ[ξψ], Θ[ρψ]
            Θ[ρψ + 1], Θ[ϸψ] = Θ[ϸψ], Θ[ρψ + 1]
            return ρψ + 1

        def REC_SOR(ΧΨ: List[int], Σλ: int, Ϻ϶: int) -> List[int]:
            if Σλ < Ϻ϶:
                μψ = PARTITION(ΧΨ, Σλ, Ϻ϶)
                REC_SOR(ΧΨ, Σλ, μψ - 1)
                REC_SOR(ΧΨ, μψ + 1, Ϻ϶)
            return ΧΨ

        πℓ = REC_SOR(πℓ, 0, len(πℓ) - 1)
        return πℓ[len(πℓ) - λβ : len(πℓ)]