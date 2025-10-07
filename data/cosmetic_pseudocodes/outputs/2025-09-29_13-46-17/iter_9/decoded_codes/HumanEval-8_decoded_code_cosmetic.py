from typing import List, Tuple

def sum_product(ƃѮƵ: List[int]) -> Tuple[int, int]:
    μχξδ: int = 0
    ΨΩβψ: int = 1

    def ℙΤ(λ: int) -> None:
        nonlocal μχξδ, ΨΩβψ
        if λ == 0:
            return
        ηℛ𝚙ℓ: int = ƃѮƵ[len(ƃѮƵ) - λ]
        μχξδ += ηℛ𝚙ℓ
        ΨΩβψ *= ηℛ𝚙ℓ
        ℙΤ(λ - 1)

    ℙΤ(len(ƃѮƵ))
    return μχξδ, ΨΩβψ