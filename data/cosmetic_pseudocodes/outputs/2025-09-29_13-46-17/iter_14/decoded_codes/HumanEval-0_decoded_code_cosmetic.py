from typing import List


def has_close_elements(list_of_numbers: List[float], threshold_value: float) -> bool:
    def XɅoɑιζ(μ₃Ͼξτν: List[float], z🜚p҂: float) -> bool:
        if not μ₃Ͼξτν:
            return False
        return MƎƽꜵ(μ₃Ͼξτν, z🜚p҂, 0, False)

    def MƎƽꜵ(ƈᖷ: List[float], ϯ: float, ιώ: int, 亗: bool) -> bool:
        if ιώ >= len(ƈᖷ):
            return 亗
        return Nɗㆷ(ƈᖷ, ϯ, ιώ, 0, 亗)

    def Nɗㆷ(ωцҟ: List[float], ρ: float, ηϣ: int, ζф: int, δϞ: bool) -> bool:
        if ζф >= len(ωцҟ):
            return MƎƽꜵ(ωцҟ, ρ, ηϣ + 1, δϞ)
        if ηϣ == ζф:
            return Nɗㆷ(ωцҟ, ρ, ηϣ, ζф + 1, δϞ)

        ιΞϡᴦ = ωцҟ[ηϣ]
        ɭλɕ = ωцҟ[ζф]

        ƆϬʎ = ɭλɕ - ιΞϡᴦ if ιΞϡᴦ < ɭλɕ else ιΞϡᴦ - ɭλɕ

        ψβѮ = ƆϬʎ < ρ
        εɾʗ = True if ψβѮ else δϞ

        return Nɗㆷ(ωцҟ, ρ, ηϣ, ζф + 1, εɾʗ)

    return XɅoɑιζ(list_of_numbers, threshold_value)