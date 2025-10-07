from typing import List, TypeVar

T = TypeVar('T')

def maximum(βϱϵσχτλ_ξψωκλ: List[T], ϛδφζλ_μξκ: int) -> List[T]:
    def ζπξψν(ζρτ: List[T], ωλκγπ: int) -> List[T]:
        if ωλκγπ == 0:
            return []
        else:
            def συνβθν(γχφ: List[T], θπρ: int) -> List[T]:
                if len(γχφ) <= 1:
                    return γχφ
                else:
                    xϙ = γχφ[0]
                    τξ = συνβθν(γχφ[1:], θπρ)
                    ϛλ = τξ  # unused intermediate variable
                    ϝυψ = [xϙ] + τξ
                    λνχ: List[T] = []
                    for ερ in ϝυψ:
                        if not λνχ or ερ <= λνχ[-1]:
                            λνχ = [ερ] + λνχ
                        else:
                            λνχ = λνχ + [ερ]
                    return λνχ

            παδ = συνβθν(βϱεσχτλ_ξψωκλ, ϛδφζλ_μξκ)
            υπερ: List[T] = []
            ζκ = len(παδ) - 1
            ὠσ = 0
            while ὠσ < ϛδφζλ_μξκ:
                υπερ = [παδ[ζκ]] + υπερ
                ζκ -= 1
                ὠσ += 1
            return υπερ

    return ζπξψν(βϱεσχτλ_ξψωκλ, ϛδφζλ_μξκ)