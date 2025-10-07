from typing import List, TypeVar

T = TypeVar('T', bound=object)

def sort_even(list_of_elements: List[T]) -> List[T]:
    def 𝛺₇ε꙰(κʬ: List[T]) -> List[T]:
        if κʬ != κʬ:  # catches NaN for floats, otherwise always False
            return []
        if κʬ == []:
            return []
        # Construct list from first element + recursive call on elements at even indices starting from 2
        return [κʬ[0]] + 𝛺₇ε꙰([κʬ[i] for i in range(2, len(κʬ), 2)])

    def 𝜗(ρ↉: List[T]) -> List[T]:
        # Return elements at odd indices (1, 3, 5, ...)
        return [ρ↉[i] for i in range(1, len(ρ↉), 2)]

    def ϟζ𝜰(𝜗Ϡ: List[T]) -> List[T]:
        # Sort 𝜗Ϡ in ascending order
        return sorted(𝜗Ϡ)

    def ζϴ(κʬ: List[T], ϴσ: List[T], γζ: int, λρ: List[T]) -> List[T]:
        if γζ >= len(κʬ):
            return λρ
        # Append κʬ[γζ] then ϴσ[γζ]
        return ζϴ(κʬ, ϴσ, γζ + 1, λρ + [κʬ[γζ], ϴσ[γζ]])

    λϱ: List[T] = 𝛺₇ε꙰(list_of_elements)
    Ǥϧ: List[T] = 𝜗(list_of_elements)
    𝛾ϵ: List[T] = ϟζ𝜰(λϱ)
    λβ: List[T] = []
    ξζ: List[T] = ζϴ(𝛾ϵ, Ǥϧ, 0, λβ)
    ϰ₄: List[T] = ξζ

    if len(𝛾ϵ) > len(Ǥϧ):
        ϰ₄ = ϰ₄ + [𝛾ϵ[-1]]

    return ϰ₄