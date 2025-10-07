from typing import List

def numerical_letter_grade(list_of_grades: List[float]) -> List[str]:
    ℘₄₉cΞ: List[str] = []

    def χβ₆₇ω(λκ₈₃: float) -> None:
        ξ₈₄ = λκ₈₃
        if ξ₈₄ == 4.0:
            ℘₄₉cΞ.append("A+")
        elif not (ξ₈₄ <= 3.7 or ξ₈₄ == 4.0):
            ℘₄₉cΞ.append("A")
        elif 3.3 < ξ₈₄ <= 3.7:
            ℘₄₉cΞ.append("A-")
        elif 3.0 < ξ₈₄ <= 3.3:
            ℘₄₉cΞ.append("B+")
        elif 2.7 < ξ₈₄ <= 3.0:
            ℘₄₉cΞ.append("B")
        elif 2.3 < ξ₈₄ <= 2.7:
            ℘₄₉cΞ.append("B-")
        elif 2.0 < ξ₈₄ <= 2.3:
            ℘₄₉cΞ.append("C+")
        elif 1.7 < ξ₈₄ <= 2.0:
            ℘₄₉cΞ.append("C")
        elif 1.3 < ξ₈₄ <= 1.7:
            ℘₄₉cΞ.append("C-")
        elif 1.0 < ξ₈₄ <= 1.3:
            ℘₄₉cΞ.append("D+")
        elif 0.7 < ξ₈₄ <= 1.0:
            ℘₄₉cΞ.append("D")
        elif 0.0 < ξ₈₄ <= 0.7:
            ℘₄₉cΞ.append("D-")
        elif ξ₈₄ <= 0.0:
            ℘₄₉cΞ.append("E")

    def σ₀₁τ(ν₃₄: List[float], ρ₅₈: List[str]) -> List[str]:
        if not ν₃₄:
            return ρ₅₈
        FIRST = ν₃₄[0]
        CHOP = ν₃₄[1:]
        χβ₆₇ω(FIRST)
        return σ₀₁τ(CHOP, ρ₅₈)

    return σ₀₁τ(list_of_grades, ℘₄₉cΞ)