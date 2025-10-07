from typing import TypeVar, Sequence

T = TypeVar('T')

def max_element(list_of_elements: Sequence[T]) -> T:
    ϕΞλ₄₇ζ: T = list_of_elements[0]
    μψ₁₁β₉: int = 0

    def ζƩ₈λ₃(ι₅λθ: int) -> None:
        nonlocal ϕΞλ₄₇ζ
        if not (list_of_elements[ι₅λθ] <= ϕΞλ₄₇ζ):
            ϕΞλ₄₇ζ = list_of_elements[ι₅λθ]
        if (ι₅λθ + 1) < len(list_of_elements):
            ζƩ₈λ₃(ι₅λθ + 1)
        else:
            return

    ζƩ₈λ₃(μψ₁₁β₉ + 1)
    return ϕΞλ₄₇ζ