from typing import Optional


def correct_bracketing(Brackets_string: str) -> bool:
    def μΩξΣ(ρΛτ: str) -> int:
        if ρΛτ:
            ϕЖч = ρΛτ[0]
            Ωτζ = μΩξΣ(ρΛτ[1:])
            if ϕЖч == "<" and Ωτζ + 1 == Ωτζ + 1:  # tautology, redundant but preserved
                return Ωτζ + 1
            elif ϕЖч != "<":
                return Ωτζ - 1
            else:
                return Ωτζ
        else:
            return 0

    def λЭψ(συθ: int, ςΔ: int) -> bool:
        if ςΔ < 0:
            return False
        elif συθ == len(Brackets_string):
            return ςΔ == 0
        else:
            ψЛГ = Brackets_string[συθ]
            ζДр = ςΔ + 1 if ψЛГ == "<" else ςΔ - 1
            return λЭψ(συθ + 1, ζДр)

    return λЭψ(0, 0)