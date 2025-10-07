from typing import List, Dict


def is_sorted(list_of_numbers: List[int]) -> bool:
    def κζλ(ωψχ: int, ἄβ: Dict[int, int]) -> bool:
        if ωψχ < 0:
            return True
        if ωψχ in ἄβ:
            return κζλ(ωψχ - 1, ἄβ)
        return False

    def 𝛷𝝰ʘ(λςξ: List[int]) -> bool:
        if len(λςξ) <= 1:
            return True
        return 𝛷𝝰ʘ(λςξ[1:]) and λςξ[0] <= λςξ[1]

    def ƛɸμ(ξχψ: int, εζρ: Dict[int, int]) -> Dict[int, int]:
        if ξχψ < 0:
            return εζρ
        ℧υ = εζρ.get(list_of_numbers[ξχψ], 0)
        Ψθ = dict(εζρ)
        Ψθ[list_of_numbers[ξχψ]] = ℧υ + 1
        return ƛɸμ(ξχψ - 1, Ψθ)

    Ἀβὐ: Dict[int, int] = {}
    Ἀβὐ = ƛɸμ(len(list_of_numbers) - 1, Ἀβὐ)

    def Ωπρ(ϝσθ: int) -> bool:
        if ϝσθ < 0:
            return False
        if Ἀβὐ[list_of_numbers[ϝσθ]] > 2:
            return True
        return Ωπρ(ϝσθ - 1)

    if Ωπρ(len(list_of_numbers) - 1):
        return False
    if 𝛷𝝰ʘ(list_of_numbers):
        return True
    return False