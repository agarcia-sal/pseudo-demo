from typing import List, TypeVar

T = TypeVar('T')


def sort_third(list_input: List[T]) -> List[T]:
    arr = Σξₓ(list_input)
    indexes = [j for j in range(len(arr)) if j % 3 == 0]
    sorted_values = μ_sort_asc(arr, 0, len(arr))
    λ_replace(arr, indexes, sorted_values, 0)
    return arr


def Σξₓ(Ξ: List[T]) -> List[T]:
    Ξ_prime: List[T] = []

    def recur_add(ζ: int) -> None:
        if ζ >= len(Ξ):
            return
        if ζ % 3 == 0:
            Ξ_prime.append(Ξ[ζ])
        recur_add(ζ + 1)

    recur_add(0)
    return Ξ_prime


def μ_sort_asc(Π: List[T], α: int, β: int) -> List[T]:
    if β <= α + 1:
        return Π[α:β]
    γ = α + ((β - α) // 2)
    left_half = μ_sort_asc(Π, α, γ)
    right_half = μ_sort_asc(Π, γ, β)

    def merge(Λ: List[T], Ξ: List[T]) -> List[T]:
        Φ: List[T] = []
        ι, ρ = 0, 0
        while ι < len(Λ) or ρ < len(Ξ):
            if ι == len(Λ):
                Φ.append(Ξ[ρ])
                ρ += 1
            elif ρ == len(Ξ):
                Φ.append(Λ[ι])
                ι += 1
            elif Λ[ι] <= Ξ[ρ]:
                Φ.append(Λ[ι])
                ι += 1
            else:
                Φ.append(Ξ[ρ])
                ρ += 1
        return Φ

    return merge(left_half, right_half)


def λ_replace(Ψ: List[T], 𝙸: List[int], 𝚆: List[T], ω: int) -> None:
    if ω == len(𝚆):
        return
    if ω == len(𝙸):
        return
    Ψ[𝙸[ω]] = 𝚆[ω]
    λ_replace(Ψ, 𝙸, 𝚆, ω + 1)