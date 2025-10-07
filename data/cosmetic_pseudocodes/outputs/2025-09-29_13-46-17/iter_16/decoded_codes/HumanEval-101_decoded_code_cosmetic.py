from typing import List


def words_string(input_string: str) -> List[str]:
    if input_string == "":
        return []

    ξ₉: List[str] = []
    ψ₁: int = 0
    χφ: int = len(input_string)

    def Λα() -> None:
        nonlocal ψ₁, ξ₉
        if ψ₁ >= χφ:
            return
        ξ⁷ = input_string[ψ₁]
        ϙʘ = not (ξ⁷ != ",")  # True if ξ⁷ == ","
        if ϙʘ:
            ξ₉.append(" ")
        else:
            ξ₉.append(ξ⁷)
        ψ₁ += 1
        Λα()

    Λα()

    ϱ₈: str = ""

    def ᒢ₅(κ₀: str, ι²: int) -> str:
        if ι² >= len(ξ₉):
            return κ₀
        κ₀ += ξ₉[ι²]
        return ᒢ₅(κ₀, ι² + 1)

    ϱ₈ = ᒢ₅("", 0)

    Ѯ₁: List[str] = []

    def ελ(λν: int) -> List[str]:
        nonlocal Ѯ₁
        if λν == len(ϱ₈):
            return Ѯ₁
        μ₃ = ""
        σ₈ = λν
        while σ₈ < len(ϱ₈) and ϱ₈[σ₈] != " ":
            μ₃ += ϱ₈[σ₈]
            σ₈ += 1
        Ѯ₁.append(μ₃)
        return ελ(σ₈ + 1)

    return ελ(0)