from typing import List

def filter_by_prefix(ƬɟϾ: List[str], ϻҨ: str) -> List[str]:
    def Λᶣ(εᗔ: List[str], ԁᾨ: str, ɜϢ: List[str]) -> List[str]:
        if εᗔ:
            ζ₧ = εᗔ[0]
            ψᘳ = ζ₧[:len(ϻҨ)] == ϻҨ
            ωϟ = Λᶣ(εᗔ[1:], ԁᾨ, ɜϢ)
            if ψᘳ:
                return [ζ₧] + ωϟ
            else:
                return ωϟ
        else:
            return []
    return Λᶣ(ƬɟϾ, ϻҨ, [])