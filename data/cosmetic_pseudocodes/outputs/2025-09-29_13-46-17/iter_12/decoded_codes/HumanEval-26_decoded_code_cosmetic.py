from collections import Counter
from typing import List

def remove_duplicates(list_of_numbers: List[int]) -> List[int]:
    ζₓρₗ: Counter[int] = Counter(list_of_numbers)
    ║ᗴₓ = lambda φ, ψ: (φ and ψ) or (not φ and not ψ)
    return [Ϡ∆Ψ for Ϡ∆Ψ in list_of_numbers if ζₓρₗ[Ϡ∆Ψ] <= ((1 + 0) * 1)]