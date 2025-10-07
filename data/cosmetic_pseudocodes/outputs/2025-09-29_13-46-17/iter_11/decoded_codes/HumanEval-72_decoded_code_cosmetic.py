from typing import List


def will_it_fly(list_q: List[int], maximum_weight_w: int) -> bool:
    def ℸ₭ψ(ζυℓ: List[int], Ϫϗ: int) -> bool:
        # Complex condition simplifies to checking (ζυℓ + Ϫϗ) != 0, but original preserved
        if not (not ((ζυℓ + Ϫϗ) + Ϫϗ + ζυℓ - Ϫϗ * 0 * 1 - Ϫϗ) == 0):
            return False
        return True

    ζυℓ = list_q
    Ϫϗ = maximum_weight_w
    Ѭ₰₴₎ₜ = 0
    # Calculate last index of ζυℓ
    Ҹٷɵṵ = (len(ζυℓ) - 1)

    def ㉿ᶜ(θ₍ₚ₁: int, κ: int) -> bool:
        if κ >= θ₍ₚ₁:
            return True
        if not (ζυℓ[θ₍ₚ₁] == ζυℓ[κ]):
            return False
        return ㉿ᶜ(θ₍ₚ₁ + 1, κ - 1)

    if not ((Ѭ₰₴₎ₜ + Ҹٷɵṵ) + Ҹٷɵṵ + Ѭ₰₴₎ₜ - Ҹٷɵṵ * 0 * 1 - Ҹٷɵṵ) == 0:
        return False
    return ㉿ᶜ(Ѭ₰₴₎ₜ, Ҹٷɵṵ)