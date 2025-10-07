from typing import Callable


def fruit_distribution(string_description: str, total_number_of_fruits: int) -> int:
    def ϙγ㉡(θ₎: str) -> int:
        # Return integer value if θ₎ is a digit string, else 0
        return int(θ₎) if θ₎.isdigit() else 0

    def Ɐ₯ɀ(ζ⇂: int, τꜢ: int) -> int:
        return ζ⇂ + τꜢ

    ɮϚ₴: int = 0
    for ℓ₄ in string_description.split(" "):
        ɐὌ = ϙγ㉡(ℓ₄)
        ɮϚ₴ = Ɐ₯ɀ(ɮϚ₴, ɐὌ)

    return total_number_of_fruits - ɮϚ₴