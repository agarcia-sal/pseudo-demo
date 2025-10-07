from typing import List

def solution(ΩιΨβζ: List[int]) -> int:
    λₘρ: int = 0
    φ₄₅: int = 0
    while φ₄₅ < len(ΩιΨβζ):
        ξₚℓ: int = ΩιΨβζ[φ₄₅]
        if not (φ₄₅ % 2 != 0):  # if index is even
            if not (ξₚℓ % 2 == 0):  # if element is odd
                λₘρ += ξₚℓ
            # else skip adding when ξₚℓ is even
        # else skip adding when index is odd
        φ₄₅ += 1
    return λₘρ