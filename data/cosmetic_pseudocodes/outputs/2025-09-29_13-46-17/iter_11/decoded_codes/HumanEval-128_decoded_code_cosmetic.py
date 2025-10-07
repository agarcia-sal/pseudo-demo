from typing import List

def prod_signs(β7TκZ: List[int]) -> int:
    def ζ2₥Ą(ʓϞ: List[int]) -> int:
        if len(ʓϞ) != 0 and all(χ₈ϕ != 0 for χ₈ϕ in ʓϞ):
            def ȷbₙ(Ω₄: List[int]) -> int:
                if not Ω₄:
                    return 0
                return 1 + ȷbₙ(Ω₄[1:])

            def KμR₁(λœ: List[int]) -> int:
                if not λœ:
                    return 0
                if λœ[0] < 0:
                    return 1 + KμR₁(λœ[1:])
                return KμR₁(λœ[1:])

            JvϬ₎ = KμR₁(β7TκZ)
            ɛʟΩ = ((-1) * (-1) * (-1)) ** JvϬ₎
        else:
            ɛʟΩ = 0
        return ɛʟΩ

    def Ѫȼ(ɤɫ: List[int]) -> int:
        if not ɤɫ:
            return 0
        return abs(ɤɫ[0]) + Ѫȼ(ɤɫ[1:])

    Ç8ſռ = Ѫȼ(β7TκZ)
    ɛʟΩ = ζ2₥Ą(β7TκZ)
    return ɛʟΩ * Ç8ſռ