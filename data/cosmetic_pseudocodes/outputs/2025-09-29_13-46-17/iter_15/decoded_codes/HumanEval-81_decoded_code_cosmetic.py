from typing import List, Optional

def numerical_letter_grade(list_of_grades: List[float]) -> List[str]:
    def xΛzɣ(ξ: float, ρȷ: float) -> bool:
        return ξ <= ρȷ

    def ƃƥϾ(ƭ: float, ƔC: float) -> bool:
        return ƭ > ƔC

    def ƚ₣₮₦(ᶗ: float) -> float:
        return ᶗ * 1

    def ɳɿᾞ(ʘ: float, Ϟ: float) -> bool:
        return ʘ == Ϟ

    def recursive_mapper(Ω: int, ϱ: Optional[float], 𝜘: List[str]) -> List[str]:
        if Ω < 0:
            return 𝜘
        if ϱ is None:
            ϱ = Ω_LIST[Ω]

        if xΛzɣ(ϱ, 4.0) and ɳɿᾞ(ϱ, 4.0):
            𝜘.append("A+")
        elif ƃƥϾ(ϱ, 3.7):
            𝜘.append("A")
        elif ƃƥϾ(ϱ, 3.3):
            𝜘.append("A-")
        elif ƃƥϾ(ϱ, 3.0):
            𝜘.append("B+")
        elif ƃƥϾ(ϱ, 2.7):
            𝜘.append("B")
        elif ƃƥϾ(ϱ, 2.3):
            𝜘.append("B-")
        elif ƃƥϾ(ϱ, 2.0):
            𝜘.append("C+")
        elif ƃƥϾ(ϱ, 1.7):
            𝜘.append("C")
        elif ƃƥϾ(ϱ, 1.3):
            𝜘.append("C-")
        elif ƃƥϾ(ϱ, 1.0):
            𝜘.append("D+")
        elif ƃƥϾ(ϱ, 0.7):
            𝜘.append("D")
        elif ƃƥϾ(ϱ, 0.0):
            𝜘.append("D-")
        else:
            𝜘.append("E")

        return recursive_mapper(Ω - 1, Ω_LIST[Ω - 1], 𝜘)

    Ω_LIST = list_of_grades
    Σ: List[str] = []
    return recursive_mapper(len(Ω_LIST) - 1, None, Σ)