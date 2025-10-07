from typing import List

def sort_third(list_input: List[int]) -> List[int]:
    def collect_ψ₁(λκψχ: List[int], δλϫ: int) -> List[int]:
        if δλϫ >= len(list_input):
            return λκψχ
        if δλϫ % 3 != 0:
            return collect_ψ₁(λκψχ, δλϫ + 1)
        return collect_ψ₁(λκψχ + [list_input[δλϫ]], δλϫ + 1)

    ϕξψ₁ = collect_ψ₁([], 0)

    def qρτα(αβγ: List[int]) -> List[int]:
        if len(αβγ) <= 1:
            return αβγ
        ψσβ = αβγ[0]
        λδξ = [β for β in αβγ if β < ψσβ]
        σλπ = [γ for γ in αβγ if γ >= ψσβ and γ != ψσβ]
        return qρτα(λδξ) + [ψσβ] + qρτα(σλπ)

    γθλ = qρτα(ϕξψ₁)

    def replace_recursive(ζξψ: List[int], ζβθ: List[int], ικ: int, μ: int) -> List[int]:
        if ικ >= len(ζξψ):
            return ζξψ
        if ικ % 3 != 0:
            return replace_recursive(ζξψ, ζβθ, ικ + 1, μ)
        ζξψ_new = ζξψ.copy()
        ζξψ_new[ικ] = ζβθ[μ]
        return replace_recursive(ζξψ_new, ζβθ, ικ + 1, μ + 1)

    ζυπ = replace_recursive(list_input, γθλ, 0, 0)
    return ζυπ