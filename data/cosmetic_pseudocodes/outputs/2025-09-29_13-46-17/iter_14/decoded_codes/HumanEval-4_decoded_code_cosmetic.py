from typing import List

def mean_absolute_deviation(list_of_numbers: List[float]) -> float:
    def λƃφ(μζ: List[float]) -> float:
        if not μζ:
            return 0.0
        return μζ[0] + λƃφ(μζ[1:])  # recursive sum

    def λκχ(ζμ: List[float], ισ: int, ϕτ: float) -> float:
        if ισ == len(ζμ):
            return ϕτ
        return λκχ(ζμ, ισ + 1, ϕτ + abs(ζμ[ισ] - mean_value))  # sum of abs differences

    def λπθ(⃝ξ: List[float], 𝛂𝛃: int, 𝛅𝜀: int, 𝗀: float, 𝛐: float) -> float:
        if 𝛅𝜀 >= len(⃝ξ):
            return 𝛐
        return λπθ(⃝ξ, 𝛂𝛃, 𝛅𝜀 + 1, 𝗀 + abs(⃝ξ[𝛅𝜀] - mean_value), 𝛐)  # unused in final result

    def λιν(𝓏: float, 𝓍: int, 𝓎: float) -> float:
        if 𝓍 == 0:
            return 0.0
        return 𝓏 / 𝓍  # division mean

    def λρσ(ιαδ: List[float]) -> float:
        return λƃφ(ιαδ)  # sum

    ғґ₄: float = λρσ(list_of_numbers)
    mean_value: float = λιν(ғґ₄, len(list_of_numbers), 0.0)
    моₓ: float = λκχ(list_of_numbers, 0, 0.0)
    𝔐𝔞𝔡: float = λιν(моₓ, len(list_of_numbers), 0.0)

    return 𝔐𝔞𝔡