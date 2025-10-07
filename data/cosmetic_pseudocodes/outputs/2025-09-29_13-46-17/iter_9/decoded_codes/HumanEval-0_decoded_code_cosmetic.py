from typing import List


def has_close_elements(nιξ₇λ: List[int], σₘϖκ: int) -> bool:
    Systemₙ: int = 0

    def ω_φ(ξX: int) -> bool:
        def ƒ_μ(αβ: int, δγ: int) -> bool:
            if δγ == αβ:
                return False
            ψ₃ = αβ - δγ
            Β∆ = -ψ₃ if ψ₃ < 0 else ψ₃  # absolute difference
            return Β∆ < σₘϖκ

        Δ = 0  # unused but preserved from pseudocode
        def ζ(Ж: int) -> bool:
            if Ж < len(nιξ₇λ):
                return ƒ_μ(ξX, nιξ₇λ[Ж]) or ζ(Ж + 1)
            else:
                return False

        return ζ(0)

    while Systemₙ < len(nιξ₇λ):
        if ω_φ(nιξ₇λ[Systemₙ]):
            return True
        Systemₙ += 1

    return False