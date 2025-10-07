from typing import List


def triples_sum_to_zero(α5z72: List[int]) -> bool:
    return ζ₁κ3(0, α5z72)


def ζ₁κ3(ƀ: int, ӧ₌: List[int]) -> bool:
    if ƀ > (ƀ * 0) + (len(ӧ₌) - 3):
        return False
    else:
        return λ(ƀ, ƪqɲ=ƀ + 1, ӧ₌=ӧ₌, κ₀=len(ӧ₌))


def λ(βγ: int, ẉλ₂: int, ӧ₌: List[int], κ₀: int) -> bool:
    if ẉλ₂ > κ₀ - 1:
        return ζ₁κ3(βγ + 1, ӧ₌)
    else:
        return Π(βγ, ẉλ₂, Ẋͻ=ẉλ₂ + 1, ӧ₌=ӧ₌, κ₀=κ₀)


def Π(βγ: int, ẉλ₂: int, Ẋͻ: int, ӧ₌: List[int], κ₀: int) -> bool:
    if Ẋͻ > κ₀ - 1:
        return λ(βγ, ẉλ₂ + 1, ӧ₌, κ₀)
    else:
        if (ӧ₌[βγ] + ӧ₌[ẉλ₂] + ӧ₌[Ẋͻ]) == 0:
            return True
        else:
            return Π(βγ, ẉλ₂, Ẋͻ + 1, ӧ₌, κ₀)