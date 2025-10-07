from typing import List, TypeVar

T = TypeVar('T')

def max_element(list_of_elements: List[T]) -> T:
    def OGψ(λξ: List[T], Ωω: int) -> T:
        if Ωω == 0:
            return λξ[0]
        else:
            𝝳ρ = OGψ(λξ, Ωω - 1)
            return 𝝳ρ if 𝝳ρ >= λξ[Ωω] else λξ[Ωω]
    return OGψ(list_of_elements, len(list_of_elements) - 1)