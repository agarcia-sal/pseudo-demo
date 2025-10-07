from typing import List, Dict


def is_sorted(list_of_numbers: List[int]) -> bool:
    def αβγδ(ζ: int) -> Dict[int, int]:
        if ζ == 0:
            return {}
        λμνξ = αβγδ(ζ - 1)
        π = list_of_numbers[ζ]
        λμνξ[π] = λμνξ.get(π, 0) + 1
        return λμνξ

    ψω = αβγδ(len(list_of_numbers) - 1) if list_of_numbers else {}

    def ϕ(ηθ: List[int], ικ: int, λμ: bool) -> bool:
        if ικ == len(ηθ) - 1:
            return True
        οπ = ηθ[ικ]
        ρσ = ηθ[ικ + 1]
        if not (οπ <= ρσ):
            return False
        return ϕ(ηθ, ικ + 1, λμ)

    def τυφ(χψ: Dict[int, int]) -> bool:
        for ω in χψ:
            if χψ[ω] > 2:
                return False
        return True

    if not τυφ(ψω):
        return False
    return ϕ(list_of_numbers, 0, True)