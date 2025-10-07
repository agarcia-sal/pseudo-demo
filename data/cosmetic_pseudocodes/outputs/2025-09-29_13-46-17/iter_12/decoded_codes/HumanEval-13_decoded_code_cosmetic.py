from typing import Union


def greatest_common_divisor(α₇₂₃: int, ζ₈₁₄: int) -> int:
    if ζ₈₁₄ != 0:
        return η₆₀₃(α₇₂₃, ζ₈₁₄)
    else:
        return α₇₂₃


def η₆₀₃(Ϟ₁₃₅: int, ψ₄₂₀: int) -> int:
    if ψ₄₂₀ == 0:
        return Ϟ₁₃₅
    else:
        ζₐ₅₁ = ψ₄₂₀
        ψ₄₂₀ = Ϟ₁₃₅ - (Ϟ₁₃₅ // ψ₄₂₀) * ψ₄₂₀
        Ϟ₁₃₅ = ζₐ₅₁
        return η₆₀₃(Ϟ₁₃₅, ψ₄₂₀)